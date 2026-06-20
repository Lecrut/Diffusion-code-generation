import numpy as np

def logical_and(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return x & y

def logical_or(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return x | y

def logical_not(x: np.ndarray) -> np.ndarray:
    return ~x

if __name__ == '__main__':
    a = np.array([True, False, True, False])
    b = np.array([False, False, True, True])

    print("AND:", logical_and(a, b))
    print("OR:", logical_or(a, b))
    print("NOT A:", logical_not(a))