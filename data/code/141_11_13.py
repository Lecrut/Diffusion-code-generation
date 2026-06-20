import numpy as np

def logical_and(a: bool, b: bool) -> bool:
    return a and b

def logical_or(a: bool, b: bool) -> bool:
    return a or b

def logical_not(a: bool) -> bool:
    return not a
if __name__ == '__main__':
    print(f'Logical AND (True, False): {logical_and(True, False)}')
    print(f'Logical AND (False, True): {logical_and(False, True)}')
    print(f'Logical AND (True, True): {logical_and(True, True)}')
    print(f'Logical OR (True, False): {logical_or(True, False)}')
    print(f'Logical OR (False, True): {logical_or(False, True)}')
    print(f'Logical OR (False, False): {logical_or(False, False)}')
    print(f'Logical NOT (True): {logical_not(True)}')
    print(f'Logical NOT (False): {logical_not(False)}')
    a = np.array([True, False, True, False])
    b = np.array([False, False, True, True])
    print('\nNumpy Custom AND:')
    print(np.logical_and(a, b))
    print('\nNumpy Custom OR:')
    print(np.logical_or(a, b))
    print('\nNumpy Custom NOT:')
    print(np.logical_not(a))