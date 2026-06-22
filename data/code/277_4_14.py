def count_items(nested_list):
    total_count = 0
    for element in nested_list:
        if isinstance(element, list):
            total_count += count_items(element)
        else:
            total_count += 1
    return total_count

if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5, 6]], 7]
    print(count_items(sample_list))