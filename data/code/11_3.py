def calculate_ratio(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    else:
        return a / b
if __name__ == '__main__':
    length1 = 10
    length2 = 5
    result = calculate_ratio(length1, length2)
    print(f"Length 1: {length1}")
    print(f"Length 2: {length2}")
    print(f"Ratio: {result}")
    length1 = 10
    length2 = 0
    result = calculate_ratio(length1, length2)
    print(f"Length 1: {length1}")
    print(f"Length 2: {length2}")
    print(f"Ratio: {result}")