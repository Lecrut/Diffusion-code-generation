def calculate_weight_difference(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return abs(x - y)

if __name__ == '__main__':
    weight1 = 90.5
    weight2 = 45.2
    print(calculate_weight_difference(weight1, weight2))