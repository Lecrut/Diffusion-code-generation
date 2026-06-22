def flatten_and_print(nested_list):
    if not isinstance(nested_list, list):
        raise ValueError("Input must be a list")
    
    def recursive_flatten(sublist):
        for item in sublist:
            if isinstance(item, list):
                yield from recursive_flatten(item)
            else:
                yield item
    
    for element in recursive_flatten(nested_list):
        print(element)

if __name__ == '__main__':
    sample_data = [1, [2, 3], [4, [5, 6]], 7]
    flatten_and_print(sample_data)