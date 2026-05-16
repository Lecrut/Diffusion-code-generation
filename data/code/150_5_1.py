def filter_tuples(data, exclude_value):
    for item in data:
        if item[1] != exclude_value:
            yield item
if __name__ == '__main__':
    input_list = [(1, 'a'), (2, 'b'), (3, 'a'), (4, 'c'), (5, 'a')]
    exclude = 'a'
    result_generator = filter_tuples(input_list, exclude)
    result_list = list(result_generator)
    print(result_list)