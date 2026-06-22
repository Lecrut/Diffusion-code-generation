def kilometers_to_meters(kilometers):
    return kilometers * 1000

if __name__ == '__main__':
    sample_values = [1, 2.5, 100, 0.001]
    for value in sample_values:
        print(kilometers_to_meters(value))