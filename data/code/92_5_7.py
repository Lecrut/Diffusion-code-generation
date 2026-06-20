def flip_truth_values(iterable):
    for value in iterable:
        yield not value

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    flipped_values = list(flip_truth_values(sample_values))
    print(flipped_values)