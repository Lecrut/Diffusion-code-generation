def min_value_generator(values):
    for value in values:
        yield value

if __name__ == '__main__':
    sample_values = [5, 3, 9, 1, 4]
    gen = min_value_generator(sample_values)
    current_min = next(gen)
    for value in gen:
        if value < current_min:
            current_min = value
    print(current_min)