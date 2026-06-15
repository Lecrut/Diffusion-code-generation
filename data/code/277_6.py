def count_nested_elements(nested_list):
    count = 0
    for element in nested_list:
        if isinstance(element, list):
            count += count_nested_elements(element)
        else:
            count += 1
    return count
if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5]], 6]
    result = count_nested_elements(sample_list)
    print(result)