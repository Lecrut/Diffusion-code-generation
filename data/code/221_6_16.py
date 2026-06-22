def validate_values(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All inputs must be numbers")

def sort_three_values(a, b, c):
    validate_values(a, b, c)
    min_val = min(a, b, c)
    max_val = max(a, b, c)
    middle_val = a + b + c - min_val - max_val
    return (min_val, middle_val, max_val)

if __name__ == '__main__':
    print(sort_three_values(3, 1, 2))