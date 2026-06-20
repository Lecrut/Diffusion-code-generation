import numpy as np

def logical_and(a, b):
    return np.logical_and(a, b)

def logical_or(a, b):
    return np.logical_or(a, b)

def logical_not(a):
    return np.logical_not(a)

if __name__ == '__main__':
    a = np.array([True, False, True, False])
    b = np.array([False, False, True, True])
    print("Logical AND:")
    print(logical_and(a, b))
    print("\nLogical OR:")
    print(logical_or(a, b))
    print("\nLogical NOT:")
    print(logical_not(a))