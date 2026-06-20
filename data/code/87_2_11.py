def is_positive_and_less_than_100(value: int) -> bool:
    return value > 0 and value < 100

if __name__ == '__main__':
    test_values = [50, -10, 100, 0]
    results = {value: is_positive_and_less_than_100(value) for value in test_values}
    print(results)