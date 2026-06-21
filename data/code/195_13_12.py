def find_unique_elements(list_a, list_b):
    unique_in_a = []
    for item in list_a:
        if item not in list_b and item not in unique_in_a:
            unique_in_a.append(item)
    return unique_in_a

if __name__ == '__main__':
    sample_list1 = [5, 3, 9, 8, 7]
    sample_list2 = [3, 4, 5, 6, 7]
    result = find_unique_elements(sample_list1, sample_list2)
    print(result)