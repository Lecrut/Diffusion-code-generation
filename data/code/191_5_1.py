def combine_lists(list_a, list_b):
    for item in list_a:
        yield item
    for item in list_b:
        yield item
if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = ['a', 'b', 'c']
    result_generator = combine_lists(list_a, list_b)
    combined_list = list(result_generator)
    print(combined_list)