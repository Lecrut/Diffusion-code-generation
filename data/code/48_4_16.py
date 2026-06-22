def largest_from_sequence(values):
    iterator = iter(values)
    try:
        current_max = next(iterator)
    except StopIteration:
        return
    for value in iterator:
        if value > current_max:
            current_max = value
    yield current_max
if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = list(largest_from_sequence(sample_data))
    print(result[0])