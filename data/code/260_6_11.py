def are_elements_close(value1, value2):
    return abs(value1 - value2) < 1e-09

def find_equal_indices(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length")
    
    return [i for i, (a, b) in enumerate(zip(list1, list2)) if are_elements_close(a, b)]

if __name__ == '__main__':
    sample_list1 = [1.0, 2.5, 3.0, 4.5]
    sample_list2 = [1.0, 2.6, 3.0, 4.5]
    print(find_equal_indices(sample_list1, sample_list2))