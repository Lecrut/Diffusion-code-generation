def kilometers_to_meters(kilometers):
    return kilometers * 1000

if __name__ == '__main__':
    test_values = [1, 2.5, 100, 0.001]
    for value in test_values:
        result = kilometers_to_meters(value)
        print(result)