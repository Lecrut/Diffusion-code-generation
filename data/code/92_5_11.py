def invert_truth_values(iterable):
    for value in iterable:
        yield not value

if __name__ == '__main__':
    sample_data = [False, True, False, True]
    inverted_results = list(invert_truth_values(sample_data))
    print(inverted_results)