def are_elements_unique(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return False
        seen.add(item)
    return True

if __name__ == '__main__':
    sample_list = [7, 14, 21, 28, 35]
    print(are_elements_unique(sample_list))
    sample_list_with_duplicates = [7, 14, 21, 28, 21]
    print(are_elements_unique(sample_list_with_duplicates))