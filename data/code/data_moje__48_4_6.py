def max_yield(sequence):
    iterator = iter(sequence)
    try:
        largest = next(iterator)
    except StopIteration:
        return
    current = largest
    for item in iterator:
        if item > current:
            yield current
            current = item
    yield current

if __name__ == '__main__':
    values = [1, 5, 2, 8, 3, 9, 4, 6, 7]
    result = list(max_yield(values))
    print(result)