def kilometers_to_meters(kilometers):
    return kilometers * 1000

if __name__ == '__main__':
    sample_values = [0, 1, 5.5, 100, -3.2]
    for val in sample_values:
        print(kilometers_to_meters(val))