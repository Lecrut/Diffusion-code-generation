def validate_numeric(value):
    if not isinstance(value, (int, float)):
        raise TypeError('All inputs must be numeric (int or float) to calculate the sum.')

def calculate_sum(a, b, c):
    validate_numeric(a)
    validate_numeric(b)
    validate_numeric(c)
    return a + b + c
if __name__ == '__main__':
    print(calculate_sum(10, 5.5, 2))
    print(calculate_sum('a', 5, 3))
    print(calculate_sum(1, 2, 'three'))
    print(calculate_sum(10, 20, 30))
    print(calculate_sum(1.5, 2.5, 3.0))
    print(calculate_sum('hello', 'world', 'test'))