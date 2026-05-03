def is_positive(number: float) -> bool:
    return number > 0
if __name__ == '__main__':
    test_values = [10.5, -5, 0, 3.14159, -0.001]
    for value in test_values:
        result = is_positive(value)
        print(f"is_positive({value}) is: {result}")