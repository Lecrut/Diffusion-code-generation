def non_negative_difference(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Inputs must be numbers")
    return abs(a - b)

if __name__ == '__main__':
    x = 50
    y = 25
    print(non_negative_difference(x, y))