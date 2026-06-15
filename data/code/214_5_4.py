import itertools
def find_absolute_minimum(iterable):
    try:
        iterator = iter(iterable)
        min_val = next(iterator)
    except StopIteration:
        raise ValueError("Iterable is empty")
    for value in iterator:
        if value < min_val:
            min_val = value
    return min_val
if __name__ == '__main__':
    data1 = [5, 2, 9, 1, 7]
    result1 = find_absolute_minimum(data1)
    print(f"Minimum of {data1}: {result1}")
    def sample_generator():
        yield 10
        yield 4
        yield 20
        yield 1
        yield 15
    gen = sample_generator()
    result2 = find_absolute_minimum(gen)
    print(f"Minimum of generator: {result2}")
    data3 = []
    try:
        result3 = find_absolute_minimum(data3)
        print(f"Minimum of {data3}: {result3}")
    except ValueError as e:
        print(f"Error for {data3}: {e}")
    data4 = [-10, 50, -3, 100]
    result4 = find_absolute_minimum(data4)
    print(f"Minimum of {data4}: {result4}")