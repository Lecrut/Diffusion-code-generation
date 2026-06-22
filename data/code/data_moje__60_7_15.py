MINUS_ONE = -1
DEFAULT_RESULT = 1

def compute_factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    def loop_multiply(start, end):
        acc = 1
        for current in range(start, end + 1):
            acc *= current
        return acc

    if n <= 1:
        return DEFAULT_RESULT
    return loop_multiply(2, n)

SAMPLE_VALUES = [0, 1, 5, 10, 25]

if __name__ == '__main__':
    for val in SAMPLE_VALUES:
        print(compute_factorial(val))
    
    try:
        compute_factorial(-5)
    except ValueError as e:
        print(e)
    
    try:
        compute_factorial(3.5)
    except TypeError as e:
        print(e)