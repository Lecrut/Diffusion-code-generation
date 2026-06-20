import numpy as np
TRUE = True
FALSE = False

def logical_and(a, b):
    return np.logical_and(a, b)

def logical_or(a, b):
    return np.logical_or(a, b)

def logical_not(a):
    return np.logical_not(a)
if __name__ == '__main__':
    sample_a = np.array([TRUE, FALSE, TRUE, FALSE])
    sample_b = np.array([FALSE, FALSE, TRUE, TRUE])
    print('AND:', logical_and(sample_a, sample_b))
    print('OR:', logical_or(sample_a, sample_b))
    print('NOT A:', logical_not(sample_a))