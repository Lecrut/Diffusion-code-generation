def count_elements(item):
    if isinstance(item, list):
        total = 0
        for sub_item in item:
            total += count_elements(sub_item)
        return total
    else:
        return 1
if __name__ == '__main__':
    sample_data = [1, [2, 3], [[4, 5], 6]]
    result = count_elements(sample_data)
    print(result)