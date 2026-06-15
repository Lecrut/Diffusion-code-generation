def filter_allowed_items(input_list, allowed_items):
    for item in input_list:
        if item in allowed_items:
            yield item
if __name__ == '__main__':
    sample_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sample_allowed = {1, 3, 5, 7, 9}
    result_generator = filter_allowed_items(sample_input, sample_allowed)
    result_list = list(result_generator)
    print(result_list)