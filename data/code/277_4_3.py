def count_items(nested_list):
    total = 0
    for item in nested_list:
        if isinstance(item, list):
            total += count_items(item)
        else:
            total += 1
    return total
if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5, 6]], 7]
    print(count_items(sample_list))