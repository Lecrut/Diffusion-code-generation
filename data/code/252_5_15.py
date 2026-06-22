def validate_lists(list1, list2):
    if not all(isinstance(item, (int, float)) for item in list1 + list2):
        raise ValueError("Both lists must contain only integers or floats.")
    return True

def compare_sums(list1, list2):
    validate_lists(list1, list2)
    sum1 = sum(list1)
    sum2 = sum(list2)
    return sum1 == sum2

if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [5, 6, 7, 8]
    result = compare_sums(list_a, list_b)
    print(result)