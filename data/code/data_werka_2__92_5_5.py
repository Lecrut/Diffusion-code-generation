def opposite_truth_values(iterable):
    for value in iterable:
        yield not value

if __name__ == '__main__':
    sample_data = [True, False, True, False, True]
    result = list(opposite_truth_values(sample_data))
    print(result)