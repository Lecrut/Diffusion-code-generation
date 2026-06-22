def are_elements_unique(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return False
        seen.add(item)
    return True
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = are_elements_unique(sample_list)
    print(result)
    sample_list_with_duplicates = [1, 2, 3, 3, 5]
    result_with_duplicates = are_elements_unique(sample_list_with_duplicates)
    print(result_with_duplicates)