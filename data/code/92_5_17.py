def opposite_truth(iterable):
    for value in iterable:
        if not isinstance(value, bool):
            raise ValueError("All elements must be boolean values")
        yield not value

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    try:
        for result in opposite_truth(sample_values):
            print(result)
    except ValueError as e:
        print(e)