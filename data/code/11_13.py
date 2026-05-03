import sys
def calculate_ratio(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
if __name__ == '__main__':
    length1 = 10
    length2 = 5
    if length1 <= 0 or length2 <= 0:
        print("Error: Both lengths must be positive numbers.")
    else:
        ratio = calculate_ratio(length1, length2)
        print(f"Length 1: {length1}")
        print(f"Length 2: {length2}")
        print(f"Ratio (Length 1 / Length 2): {ratio}")