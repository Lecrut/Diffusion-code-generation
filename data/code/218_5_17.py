def min_generator(values):
    for value in values:
        yield value

if __name__ == '__main__':
    sample_values = [5, 3, 9, 1, 10]
    min_gen = min_generator(sample_values)
    current_min = next(min_gen)
    for value in min_gen:
        if value < current_min:
            current_min = value
    print(current_min)