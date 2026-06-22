def flatten_and_print(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_and_print(item)
        else:
            yield item

if __name__ == '__main__':
    sample_data = [1, ['a', 'b'], ['c', ['d', 'e']], 9]
    for element in flatten_and_print(sample_data):
        print(element)