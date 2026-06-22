def kilometers_to_meters(kilometers):
    return kilometers * 1000

if __name__ == '__main__':
    test_values = [0, 1, 2.5, 100]
    for km in test_values:
        print(kilometers_to_meters(km))