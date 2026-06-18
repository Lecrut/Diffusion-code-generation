def compare_floats(a: float, b: float, tol: float = 1e-9) -> bool:
    return abs(a - b) <= tol
    
if __name__ == '__main__':
    print(compare_floats(0.1 + 0.2, 0.3))