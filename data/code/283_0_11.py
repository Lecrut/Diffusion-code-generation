def are_elements_unique(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return False
        seen.add(item)
    return True

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = are_elements_unique(sample_list)
    print(result)

    sample_list_with_duplicates = [10, 20, 30, 30, 50]
    result_with_duplicates = are_elements_unique(sample_list_with_duplicates)
    print(result_with_duplicates)