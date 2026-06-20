import numpy as np

def logical_and(A, B):
    return np.logical_and(A, B)

def logical_or(A, B):
    return np.logical_or(A, B)

def logical_not(A):
    return np.logical_not(A)

if __name__ == '__main__':
    a = np.array([True, False, True, False])
    b = np.array([False, False, True, True])
    print("AND:", logical_and(a, b))
    print("OR:", logical_or(a, b))
    print("NOT A:", logical_not(a))