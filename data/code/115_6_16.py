def validate_pairs(pairs):
    for num1, num2 in pairs:
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise TypeError("Both elements of the pair must be numbers")
        if num2 == 0:
            raise ValueError("Division by zero is not allowed")

def divide_pairs(pairs):
    validate_pairs(pairs)
    for a, b in pairs:
        yield a / b

if __name__ == '__main__':
    sample_pairs = [(4, 2), (9, 3), (10, 5)]
    for result in divide_pairs(sample_pairs):
        print(result)