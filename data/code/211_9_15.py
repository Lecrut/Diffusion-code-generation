def compare_lists(list1, list2):
    if not all(isinstance(x, float) for x in list1 + list2):
        raise ValueError("Both lists must contain only floats.")
    
    return [i for i, (a, b) in enumerate(zip(list1, list2)) if abs(a - b) > 0.01]

if __name__ == '__main__':
    sample_list1 = [1.01, 2.05, 3.03, 4.07]
    sample_list2 = [1.00, 2.06, 3.02, 4.08]
    print(compare_lists(sample_list1, sample_list2))