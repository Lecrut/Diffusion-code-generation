def find_max_in_nested_list(nested_list):
    def flatten(lst):
        for item in lst:
            if isinstance(item, (list, tuple)):
                yield from flatten(item)
            else:
                yield item

    return max(flatten(nested_list))

if __name__ == '__main__':
    sample_data = [1, [2, 3], [[4, 5], [6, [7, 8]]], 9]
    result = find_max_in_nested_list(sample_data)
    print(result)