def find_largest(generator):
    try:
        largest = next(generator)
    except StopIteration:
        raise ValueError('Input generator cannot be empty')
    for item in generator:
        if item > largest:
            largest = item
    return largest
if __name__ == '__main__':
    sample_generator = (x * x for x in range(10))
    result = find_largest(sample_generator)
    print(result)