import math

def are_floats_close(a, b, rel_tol=1e-09, abs_tol=0.0):
    return math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)

if __name__ == '__main__':
    value1 = 1.1
    value2 = 1.100000001
    print(f"Is {value1} equal to {value2}? {are_floats_close(value1, value2)}")
    
    value3 = float('inf')
    value4 = float('-inf')
    print(f"Is {value3} equal to {value4}? {are_floats_close(value3, value4)}")
    
    value5 = float('nan')
    value6 = float('nan')
    print(f"Is {value5} equal to {value6}? {are_floats_close(value5, value6)}")