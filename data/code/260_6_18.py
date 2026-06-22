def find_equal_indices(list1, list2):
    if not all(isinstance(x, float) for x in list1 + list2):
        raise ValueError("Both lists must contain only floating-point numbers.")
    
    return [i for i, (a, b) in enumerate(zip(list1, list2)) if a == b]

if __name__ == '__main__':
    sample_list1 = [1.0, 2.5, 3.0, 4.5]
    sample_list2 = [1.0, 2.6, 3.0, 4.5]
    print(find_equal_indices(sample_list1, sample_list2))