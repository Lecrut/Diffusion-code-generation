def get_nth_generator_value(generator, n):
    for i, value in enumerate(generator):
        if i == n:
            return value
    raise IndexError("Index out of range")

if __name__ == '__main__':
    sample_generator = (x * x for x in range(100))
    target_index = 5
    result = get_nth_generator_value(sample_generator, target_index)
    print(result)