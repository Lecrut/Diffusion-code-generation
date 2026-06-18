def is_positive(result):
    if result > 0:
        return True
    return False
if __name__ == '__main__':
    test_values = [10, -5, 0]
    for val in test_values:
        print(f"{val}: {is_positive(val)}")