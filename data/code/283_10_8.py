def are_elements_unique(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return False
        seen.add(item)
    return True
if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_list_2 = [1, 2, 3, 3, 5]
    print(are_elements_unique(sample_list_1))
    print(are_elements_unique(sample_list_2))