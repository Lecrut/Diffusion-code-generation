import math

def are_floats_close(a, b, rel_tol=1e-09, abs_tol=0.0):
    return math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)

if __name__ == '__main__':
    value1 = 3.141592653589793
    value2 = 3.141592653589794
    print(f"Are {value1} and {value2} close? {are_floats_close(value1, value2)}")

    value3 = float('inf')
    value4 = float('-inf')
    print(f"Are both infinities equal? {are_floats_close(value3, value4)}")

    value5 = float('nan')
    value6 = float('nan')
    print(f"Are both NaNs equal? {are_floats_close(value5, value6)}")