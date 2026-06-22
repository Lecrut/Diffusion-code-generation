def flatten_and_find_max(nested_list):
    def flatten(lst):
        flat = []
        for item in lst:
            if isinstance(item, (list, tuple)):
                flat.extend(flatten(item))
            else:
                flat.append(item)
        return flat

    flat_list = flatten(nested_list)
    return max(flat_list)

if __name__ == '__main__':
    sample_data = [1, [2, 3], [[4, 5], [6, [7, 8]]], 9, [10, [11, [12, 13]]]]
    result = flatten_and_find_max(sample_data)
    print(result)