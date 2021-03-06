# coding: utf-8
u"""
    Base class of Greedy algorithms
"""
import numpy as np



class Greedy:
    u"""
    base class of Greedy algorithms
    [args]
        A: measurement matrix (2d ndarray)
        y: measured vector    (1d ndarray)
    [return]
        recovered vector      (1d ndarray)
    """
        
    def __init__(self, A, y):

        self.A  = A 
        self.n  = A.shape[1]
        self.y  = y
        self.e  = float("inf") 

        # Initialization 
        self.z  = np.zeros(self.n, dtype=np.complex)
        self.r  = self.y

        # Constants about convergence
        self.EPS            = 10**-5        # acceptable residual
        self.ITER_MAX       = 1*10**1  # max of iterations 
        
        self.name           = "Unknown"
        self.iterations     = 0  # iterator var
        
        # Options
        self.logging        = True



    def __iter__(self):
        return self
         
    def next(self):
        
        # check number of loops
        if self.iterations == self.ITER_MAX:
            if self.logging:
                print "Reach to MAX Iterations"
                print self.get_result()
            raise StopIteration
        
        # check convergence by previous iteration
        if self.e < self.EPS:
            if self.logging:
                print "Converged"
                print self.get_result()
            raise StopIteration

        # iterate 
        self.iterations += 1 
        self.z  = self.iterate()

        # return signal estimated by n-iterations 
        self.r  = self.y - np.dot(self.A, self.z)
        self.e  = np.linalg.norm(self.r) / np.linalg.norm(self.y)
        return self.z
   
    def get_last(self):
        
        return [i for i in self][-1]  


    def set_epsilon(self, e):
        self.EPS = e
        
  
    def set_maxiterations(self, num):
        self.ITER_MAX = num


    def get_status(self):
        
        status =  "" 
        status += "iterations:        %d\n"    % self.iterations
        status += "residual norm (e): %.2e\n"  % self.e
        return status
    
    def get_result(self):
        
        result  = "------- summary ------\n"
        result += "[ %s ]\n"                    % self.name
        result += "number of iterations: %d\n"  % self.iterations 
        result += "specified error:   %.2e\n"   % self.EPS
        result += "residual norm (e): %.2e\n"   % self.e
        return result
 
    def activate_logging(self):
        self.logging        = True
    
    def deactivate_logging(self):
        self.logging        = False
          
