def middle_element(iterable):
    iterator = iter(iterable)
    try:
        first = next(iterator)
        second = next(iterator)
    except StopIteration:
        return None
    for _ in range(1, len(iterable) // 2 - 1):
        try:
            next(iterator)
        except StopIteration:
            break
    else:
        return second
    try:
        third = next(iterator)
    except StopIteration:
        return first
    return (second + third) / 2
if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(middle_element(sample_values))