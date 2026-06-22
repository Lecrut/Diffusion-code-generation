def kilometers_to_miles(kilometers):
    return kilometers * 5

if __name__ == '__main__':
    sample_values = [10, 100, 0.5, 25]
    for value in sample_values:
        print(kilometers_to_miles(value))