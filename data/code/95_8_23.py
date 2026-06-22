def is_positive(n):
    return n > 0

def is_even(n):
    return n % 2 == 0

def is_less_than_100(n):
    return n < 100

def validate_number(n):
    if not isinstance(n, (int, float)):
        raise ValueError("Input must be a number")
    if not is_positive(n):
        return "Not positive"
    if not is_even(n):
        return "Odd"
    if not is_less_than_100(n):
        return "Too large"
    return "Positive, even, and less than 100"

if __name__ == '__main__':
    samples = [20, -1, 30, 100, 99]
    for s in samples:
        print(validate_number(s))