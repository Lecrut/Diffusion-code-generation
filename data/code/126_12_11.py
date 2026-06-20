import math

def are_floats_close(a, b, rel_tol=1e-09, abs_tol=0.0):
    return math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)

if __name__ == '__main__':
    value1 = 3.14
    value2 = 3.1400000000000004
    print(f"Are {value1} and {value2} close? {are_floats_close(value1, value2)}")
    
    value3 = float('inf')
    value4 = float('inf')
    print(f"Are {value3} and {value4} close? {are_floats_close(value3, value4)}")
    
    value5 = float('nan')
    value6 = float('nan')
    print(f"Are {value5} and {value6} close? {are_floats_close(value5, value6)}")