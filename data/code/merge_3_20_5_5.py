import math
def equal_approximate(a: float, b: float) -> bool: return abs(a - b) < 1e-6
if __name__ == '__main__': print(equal_approximate(0.1 + 0.2, 0.3))