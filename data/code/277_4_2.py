def count_items(nested_list):
    count = 0
    for item in nested_list:
        if isinstance(item, list):
            count += count_items(item)
        else:
            count += 1
    return count
if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5, 6], 7], 8]
    print(count_items(sample_list))