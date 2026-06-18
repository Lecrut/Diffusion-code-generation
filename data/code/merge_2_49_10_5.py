def check_positive(value: float) -> bool:
    return value > 0
if __name__ == '__main__':
    test_values = [10.5, -3, 0]
    for val in test_values:
        result = check_positive(val)
        print(f"{val}: {'positive' if result else 'not positive'}")