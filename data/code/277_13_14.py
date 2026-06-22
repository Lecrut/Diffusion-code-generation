def count_elements(nested_list):
    total = 0
    for item in nested_list:
        if isinstance(item, list):
            total += count_elements(item)
        else:
            total += 1
    return total

if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5, 6]], 7]
    result = count_elements(sample_list)
    print(result)