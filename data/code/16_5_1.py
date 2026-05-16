def filter_positives(input_iterable):
    for number in input_iterable:
        if number > 0:
            yield True
if __name__ == '__main__':
    sample_data = [-1, 0, 5, -3, 10, 0.5]
    result_generator = filter_positives(sample_data)
    result_list = list(result_generator)
    print(result_list)