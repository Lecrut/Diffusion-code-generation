def is_strictly_greater(num1, num2):
    try:
        return float(num1) > float(num2)
    except ValueError:
        return None

if __name__ == '__main__':
    sample_values = [(5, 3), (2.5, 3.0), ('a', 1), (4, 'b')]
    for val1, val2 in sample_values:
        result = is_strictly_greater(val1, val2)
        print(f"is_strictly_greater({val1}, {val2}) -> {result}")