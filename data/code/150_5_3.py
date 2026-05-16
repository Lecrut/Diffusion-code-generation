def filter_tuples(data, exclude_value):
    for tuple_item in data:
        if tuple_item[1] != exclude_value:
            yield tuple_item
if __name__ == '__main__':
    input_list = [(1, 'a'), (2, 'b'), (3, 'a'), (4, 'c'), (5, 'a')]
    exclude = 'a'
    filtered_generator = filter_tuples(input_list, exclude)
    result_list = list(filtered_generator)
    print(result_list)