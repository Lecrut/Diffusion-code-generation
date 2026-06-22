def compare_min_max(list1, list2):
    if not all((isinstance(x, (int, float)) for x in list1 + list2)):
        raise ValueError('Both lists must contain only numbers')
    min_val = min(min(list1), min(list2))
    max_val = max(max(list1), max(list2))
    return (min_val, max_val)
if __name__ == '__main__':
    sample_list1 = [3, 5, 1, 8]
    sample_list2 = [2, 9, 4, 7]
    result = compare_min_max(sample_list1, sample_list2)
    print(result)