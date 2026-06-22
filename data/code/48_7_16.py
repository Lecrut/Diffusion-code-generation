def find_max_in_nested_list(nested_list):
    def flatten(lst):
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(flatten(item))
            else:
                result.append(item)
        return result

    flat_list = flatten(nested_list)
    return max(flat_list)

if __name__ == '__main__':
    sample_data = [1, [2, 3], [4, [5, 6]], 7, [8, [9, [10]]]]
    print(find_max_in_nested_list(sample_data))