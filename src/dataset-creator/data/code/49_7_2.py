def is_positive(value):
    if value > 0:
        return True
    return False
if __name__ == '__main__':
    test_values = [5, -3, 0]
    for val in test_values:
        result = is_positive(val)
        print(f"{val} -> {result}")