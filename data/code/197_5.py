def filter_allowed_items(input_list, allowed_set):
    for item in input_list:
        if item in allowed_set:
            yield item
if __name__ == '__main__':
    sample_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    allowed_items = {2, 4, 6, 8, 10}
    result_generator = filter_allowed_items(sample_input, allowed_items)
    result_list = list(result_generator)
    print(result_list)