def is_strictly_greater(num1, num2):
    try:
        return float(num1) > float(num2)
    except ValueError:
        return False

if __name__ == '__main__':
    sample_values = [(5, 3), (3.5, 4.2), ('7', '6'), ('abc', 1)]
    results = [is_strictly_greater(a, b) for a, b in sample_values]
    print(results)