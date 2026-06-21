def is_even(number: int) -> bool:
    return number % 2 == 0
if __name__ == '__main__':
    test_values = [-4, -3, 0, 1, 2, 100, -100]
    for val in test_values:
        print(f'{val} is even: {is_even(val)}')