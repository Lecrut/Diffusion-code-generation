import itertools

def yield_largest(numbers):
    it = iter(numbers)
    try:
        largest = next(it)
    except StopIteration:
        return
    for number in it:
        if number > largest:
            largest = number
    yield largest

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = next(yield_largest(sample_data))
    print(result)