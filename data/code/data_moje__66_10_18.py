def kilometers_to_meters(kilometers):
    return kilometers * 1000

if __name__ == '__main__':
    sample_values = [1, 5.5, 100, 0.25]
    for value in sample_values:
        print(kilometers_to_meters(value))