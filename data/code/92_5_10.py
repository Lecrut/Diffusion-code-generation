def opposite_truth_values(iterable):
    for value in iterable:
        yield not value

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    print(list(opposite_truth_values(sample_values)))