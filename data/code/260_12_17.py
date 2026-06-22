def find_unique_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1 & set2
    unique_in_list1 = set1 - intersection
    unique_in_list2 = set2 - intersection
    return sorted(list(unique_in_list1)), sorted(list(unique_in_list2))

if __name__ == '__main__':
    sample_list_a = [1.1, 2.2, 3.3, 4.4, 5.5]
    sample_list_b = [3.3, 4.4, 5.5, 6.6, 7.7]
    
    unique_elements_a, unique_elements_b = find_unique_elements(sample_list_a, sample_list_b)
    print(f"Unique elements in List A: {unique_elements_a}")
    print(f"Unique elements in List B: {unique_elements_b}")