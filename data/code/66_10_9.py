def kilometers_to_meters(kilometers):
    return kilometers * 1000

if __name__ == '__main__':
    test_values = [0, 1, 5.5, 10, 100.25]
    for val in test_values:
        print(kilometers_to_meters(val))