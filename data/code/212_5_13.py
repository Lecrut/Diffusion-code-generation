def find_min_max(nested_list):
    def helper(sublist):
        if isinstance(sublist, list):
            return min(helper(item) for item in sublist), max(helper(item) for item in sublist)
        else:
            return sublist, sublist

    min_val, max_val = helper(nested_list)
    return min_val, max_val

if __name__ == '__main__':
    sample_data = [1, [2, 3], [[4, 5], 6], 7]
    print(find_min_max(sample_data))