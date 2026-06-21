def check_evenness(number: int) -> bool:
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    for value in test_values:
        result = check_evenness(value)
        print(result)