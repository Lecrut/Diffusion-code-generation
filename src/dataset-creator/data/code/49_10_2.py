def is_positive(value: float) -> bool:
    return value > 0
if __name__ == '__main__':
    test_cases = [10.5, -3.2, 0]
    for num in test_cases:
        result = is_positive(num)
        print(f"{num} is {'positive' if result else 'not positive'}")