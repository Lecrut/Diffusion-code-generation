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
    data1 = [5, 2, 8, 1, 9, 3]
    result1 = find_absolute_minimum(data1)
    print(f"Data: {data1}, Minimum: {result1}")
    def sample_generator():
        yield 10
        yield -5
        yield 20
        yield 0
        yield 15
    gen = sample_generator()
    result2 = find_absolute_minimum(gen)
    print(f"Generator values, Minimum: {result2}")
    try:
        data3 = []
        result3 = find_absolute_minimum(data3)
        print(f"Data: {data3}, Minimum: {result3}")
    except ValueError as e:
        print(f"Data: {data3}, Error: {e}")
    data4 = [42]
    result4 = find_absolute_minimum(data4)
    print(f"Data: {data4}, Minimum: {result4}")