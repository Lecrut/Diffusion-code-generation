def count_elements(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += count_elements(item)
        else:
            total += 1
    return total
if __name__ == '__main__':
    sample_list = [1, ['a', 'b'], [[3], 4], 5]
    result = count_elements(sample_list)
    print(result)