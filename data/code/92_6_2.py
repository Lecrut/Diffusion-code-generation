def opposite_truth_generator(iterable):
    for value in iterable:
        yield not value
if __name__ == '__main__':
    sample_iterable = [True, False, True, False, True]
    result_generator = opposite_truth_generator(sample_iterable)
    result_list = list(result_generator)
    print(result_list)