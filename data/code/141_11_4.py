import numpy as np

def custom_and(a, b):
    return np.logical_and(a, b)

def custom_or(a, b):
    return np.logical_or(a, b)

def custom_not(a):
    return np.logical_not(a)

if __name__ == '__main__':
    a = np.array([True, False, True, False])
    b = np.array([False, False, True, True])

    print("AND gate:")
    print(custom_and(a, b))

    print("\nOR gate:")
    print(custom_or(a, b))

    print("\nNOT gate:")
    print(custom_not(a))