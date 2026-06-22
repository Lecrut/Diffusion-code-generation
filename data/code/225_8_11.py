def find_min_max(generator):
    try:
        min_val = max_val = next(generator)
    except StopIteration:
        return (None, None)
    for value in generator:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    return (min_val, max_val)
if __name__ == '__main__':
    sample_gen = (x ** 2 for x in range(10))
    print(find_min_max(sample_gen))