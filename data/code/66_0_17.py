def kilometers_to_meters(kilometers):
    return kilometers * 1000

if __name__ == '__main__':
    sample_values = [1, 2.5, 0, -3, 100]
    for value in sample_values:
        result = kilometers_to_meters(value)
        print(result)