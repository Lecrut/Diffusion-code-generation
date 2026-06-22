def count_items(nested_list):
    total_count = 0
    for item in nested_list:
        if isinstance(item, list):
            total_count += count_items(item)
        else:
            total_count += 1
    return total_count
if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5, 6]], 7]
    print(count_items(sample_list))