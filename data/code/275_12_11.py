def flatten_and_print(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_and_print(item)
        else:
            yield item

if __name__ == '__main__':
    sample_data = [1, [2, 3], [4, [5, 6]], 7]
    for element in flatten_and_print(sample_data):
        print(element)