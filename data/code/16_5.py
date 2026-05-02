def filter_positives(input_iterable):
    for number in input_iterable:
        if number > 0:
            yield True
if __name__ == '__main__':
    sample_data = [1, -2, 3, 0, 5, -10, 4]
    result_generator = filter_positives(sample_data)
    result_list = list(result_generator)
    print(result_list)