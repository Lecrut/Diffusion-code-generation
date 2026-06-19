def compare_lengths(list1, list2):
    max_length = max(max(list1), max(list2))
    min_length = min(min(list1), min(list2))
    range_difference = max_length - min_length
    return {
        'max_length': max_length,
        'min_length': min_length,
        'range_difference': range_difference
    }

if __name__ == '__main__':
    list1 = [10, 20, 30, 40]
    list2 = [5, 15, 25, 35]
    result = compare_lengths(list1, list2)
    print(result)