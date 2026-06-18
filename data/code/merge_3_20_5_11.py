import math
def compare_floats(a: float, b: float, epsilon: float = 1e-9) -> bool: return abs(a - b) < epsilon
if __name__ == '__main__': print(compare_floats(3.14159265358979, 3.14159265358979))