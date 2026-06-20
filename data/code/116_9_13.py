def validate_input(a, b, c):
    if not all((isinstance(x, (int, float)) for x in [a, b, c])):
        raise TypeError('All inputs must be numeric (int or float) to calculate the sum.')

def calculate_sum(a, b, c):
    validate_input(a, b, c)
    return a + b + c
if __name__ == '__main__':
    print(calculate_sum(10, 5.5, 2))
    print(calculate_sum('a', 5, 3))