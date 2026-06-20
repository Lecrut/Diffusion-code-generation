import numpy as np
TRUE = True
FALSE = False

def custom_and(a, b):
    return np.logical_and(a, b)

def custom_or(a, b):
    return np.logical_or(a, b)

def custom_not(a):
    return np.logical_not(a)
if __name__ == '__main__':
    a = np.array([TRUE, FALSE, TRUE, FALSE])
    b = np.array([FALSE, FALSE, TRUE, TRUE])
    print('Custom AND:')
    print(custom_and(a, b))
    print('\nCustom OR:')
    print(custom_or(a, b))
    print('\nCustom NOT:')
    print(custom_not(a))