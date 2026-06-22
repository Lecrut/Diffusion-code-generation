def kilometers_to_meters(kilometers):
    return kilometers * 1000

if __name__ == '__main__':
    test_values = [1, 0.5, 10, 100]
    for km in test_values:
        print(kilometers_to_meters(km))