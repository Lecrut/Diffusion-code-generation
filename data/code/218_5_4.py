def min_generator(values):
    for value in values:
        yield value

if __name__ == '__main__':
    sample_values = [5, 3, 9, 1, 4]
    gen = min_generator(sample_values)
    min_value = next(gen)
    for value in gen:
        if value < min_value:
            min_value = value
    print(min_value)