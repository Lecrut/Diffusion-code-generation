a = 10
b = 5

def validate_numbers(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Both inputs must be numbers")

def calculate_difference(x, y):
    return x - y

if __name__ == '__main__':
    validate_numbers(a, b)
    result = calculate_difference(a, b)
    print(result)