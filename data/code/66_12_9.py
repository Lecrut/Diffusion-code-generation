def kilometers_to_meters(kilometers: int) -> int:
    return kilometers * 1000

if __name__ == '__main__':
    test_values = [1, 5, 10, 100]
    for value in test_values:
        print(kilometers_to_meters(value))