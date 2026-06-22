def max_pairs(list1, list2):
    if not all(isinstance(x, (int, float)) for x in list1 + list2):
        raise ValueError("Both lists must contain only numbers.")
    return [max(a, b) for a, b in zip(list1, list2)]

if __name__ == '__main__':
    sample_list1 = [1, 3, 5]
    sample_list2 = [2, 2, 6]
    try:
        result = max_pairs(sample_list1, sample_list2)
        print(result)
    except ValueError as e:
        print(e)