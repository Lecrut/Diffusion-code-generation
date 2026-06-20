add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y

def perform_operations(a, b):
    if not all(isinstance(i, (int, float)) for i in [a, b]):
        raise ValueError("Both inputs must be integers or floats.")
    
    return add(a, b), sub(a, b), mul(a, b), div(a, b)

if __name__ == '__main__':
    result_add, result_sub, result_mul, result_div = perform_operations(8, 2)
    print(result_add)
    print(result_sub)
    print(result_mul)
    print(result_div)