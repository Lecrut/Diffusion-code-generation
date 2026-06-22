def count_elements(nested_list):
    element_count = 0
    for item in nested_list:
        if isinstance(item, list):
            element_count += count_elements(item)
        else:
            element_count += 1
    return element_count

if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5, 6]], 7]
    print(count_elements(sample_list))