def count_elements(nested_list):
    count = 0
    for element in nested_list:
        if isinstance(element, list):
            count += count_elements(element)
        else:
            count += 1
    return count
if __name__ == '__main__':
    sample_data = [1, [2, 3], [[4, 5], 6], 7]
    print(count_elements(sample_data))