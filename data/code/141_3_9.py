import numpy as np

def logical_and(a, b):
    return np.logical_and(a, b)

def logical_or(a, b):
    return np.logical_or(a, b)

def logical_not(a):
    return np.logical_not(a)

if __name__ == '__main__':
    sample_a = np.array([True, False, True, False])
    sample_b = np.array([False, False, True, True])
    
    and_result = logical_and(sample_a, sample_b)
    or_result = logical_or(sample_a, sample_b)
    not_a_result = logical_not(sample_a)
    
    print("AND:", and_result)
    print("OR:", or_result)
    print("NOT A:", not_a_result)