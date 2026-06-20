import numpy as np

def logical_and(a, b):
    return a & b

def logical_or(a, b):
    return a | b

def logical_not(a):
    return ~a

if __name__ == '__main__':
    a = np.array([True, False, True, False])
    b = np.array([False, False, True, True])

    print("AND:", logical_and(a, b))
    print("OR:", logical_or(a, b))
    print("NOT a:", logical_not(a))