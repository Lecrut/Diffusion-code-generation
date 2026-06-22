def min_generator(values):
    for value in values:
        yield value

if __name__ == '__main__':
    sample_values = [5, 3, 9, 1, 4]
    min_value = min(min_generator(sample_values))
    print(min_value)