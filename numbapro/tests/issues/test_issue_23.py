import numpy as np
import numbapro 
from numba import autojit, jit, double, void, uint32, prange

@autojit
def test_prange_modulo(a, b):
    c = np.zeros(10)
    for i in prange(c.size):
        c[i] = a % b
    return c

if __name__ == '__main__':
    print test_prange_modulo(100, 50)

