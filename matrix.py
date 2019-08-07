import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        determinant = 0
        
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
      
        if self.h == 1: #1x1 matrix
            determinant = 1/self.g[0][0]
            
        elif self.h == 2: # 2x2 matrix
            if self.g[0][0]*self.g[1][1] == self.g[0][1]*self.g[1][0]:
                raise ValueError('The matrix is not invertible')
                
            else:
                determinant = self.g[0][0]*self.g[1][1]-self.g[0][1]*self.g[1][0]
            
        return determinant
            
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        trace = 0
        
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
                 
        if self.h == 1 : #1x1 matrix
            trace = self.g[0][0]
        elif self.h > 1 : #any size greater than 1x1 matrix
            for i in range(self.h):# 'i' represents both column and row of self
                trace += self.g[i][i]
        return trace
     

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        
        inverse = [];
        
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2")
        # TODO - your code here
        
        if self.h == 1:# 1x1 matrix
            for j in range(self.w): # width
                row = []
                for i in range(self.h): #height
                    row.append(1/self.g[i][j]) #this has row = [#] which is a list
                    inverse.append(row) # this puts inverse as = [[#]] which is a list inside a list

                # the problem that i was running into were two cases:
                # 1) when put return Matrix(inverse): it gave me an error since i was not appending a list (row) inside the other (inverse)
                # I was only creating a list inverse and never creating the list row. then would say: inverse.append(1/self[0][0])
                # would even put a bracket inside to make it list inside a list, but this doesn't work
                # 2) when put return inverse: this gave me the error "list object has no attribute g". This is because a list cannot have 
                # an attribute. Only an object or instance, so should have put Matrix(inverse) in this case
        
        elif self.h == 2 : #2x2 matrix
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]

            #determinant factor
            f = 1/self.determinant()

            # reorganized matrix
            inverse = [[d,-b],[-c,a]]
            #print('inverse:',inverse)
            
            #multiply matrix by factor to get real value of inverse matrix
            for i in range(self.h):
                for j in range(self.h):#self.h since it's a square matrix
                    inverse[i][j] = inverse[i][j]*f
                
                
        return Matrix(inverse)               
                
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here

        #accept to transpose matrices of 2x2 3x3 3x2 2x3
        selfTransp = zeroes(self.w, self.h)# sets dimensions of transpose matrix
              
        for col in range(selfTransp.w): #could be 1,2,3... rows of self matrix. Col represents the self column and SelfTranp rows in this
            self_row = []
            self_row = self.g[col] 
            for row in range(selfTransp.h): # row represents the self's rows and selfTranp's columns
                selfTransp[row][col] = self_row[row] # column of list matches with row in transposed matrix
                       
        return selfTransp
 
    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        newSelf = zeroes(self.h,self.w) #initiates matrix of same dimension as the input with zeroes in it
        
        #adds matrices with help of loop
        for i in range(self.h):
            for k in range(self.w):
                newSelf[i][k] = self[i][k] + other[i][k]
                  
        return newSelf
        

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        negative = zeroes(self.h,self.w) #initiates matrix of same dimension as the input with zeroes in it
        
        #puts a negative to each element in matrix
        for i in range(self.h):
            for k in range(self.w):
                negative[i][k] = -self[i][k]      
        
        return negative
        

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #
        # TODO - your code here
        if self.h != other.h or self.w != other.w:
            raise(ErrorValue, "Matrices cannot be subtracted if they have different dimensions")
            
        newSelf = zeroes(self.h,self.w)
        
        for i in range(self.h):
            for k in range(self.w):
                newSelf[i][k] = self[i][k] - other[i][k] 
        #
        return newSelf
        

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
                
        if self.w != other.h:
            raise(ValueError,'Matrices are not able to be multiply. the number of columns in Self and number of row in Other matrix must match')
        else:# if they do match, then multiply
            
            newSelf = zeroes(self.h,other.w)
            
            otherTransp = other.T()
            
            for i in range(self.h):# i represents the number of rows of self
                # j represents number of rows otherTransp (notice:they are not always equal with number of rows of self)
                for j in range(otherTransp.h):
                    for col in range(self.w): # col represents number of columns in self and otherTransposed (they are always equal)
                        self_row = self[i]
                        otherTransp_row = otherTransp[j]

                        # Self's row count 'i' equals to row counting of newSelf. Selftranp's row count 'j' equals newSelf's columns
                        newSelf[i][j]= newSelf[i][j] + (self_row[col]*otherTransp_row[col])
                
        return newSelf
        

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            newSelf = zeroes(self.h,self.w)
            for i in range(self.h): #repeats as many number of rows as self has
                for k in range(self.w): # repeats as many number of columns as self has
                    newSelf[i][k] = other*self[i][k]
            return newSelf
            #
            