def calculate_weight_difference(a, b):
    return abs(a - b)

if __name__ == '__main__':
    print(calculate_weight_difference(10.5, 7.3))
    print(calculate_weight_difference(5.0, 5.0))
    print(calculate_weight_difference(100.0, 0.0))
    print(calculate_weight_difference(-5.5, 5.5))
    print(calculate_weight_difference(123.456, 789.012))