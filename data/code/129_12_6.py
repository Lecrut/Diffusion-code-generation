def sort_strings_by_length_descending(string_list):
    return sorted(string_list, key=len, reverse=True)
if __name__ == '__main__':
    sample_list_1 = ["apple", "banana", "kiwi", "orange", "grapefruit"]
    result_1 = sort_strings_by_length_descending(sample_list_1)
    print(f"Original List 1: {sample_list_1}")
    print(f"Sorted List 1: {result_1}")
    sample_list_2 = ["a", "bb", "ccc", "dddd", "eeeee"]
    result_2 = sort_strings_by_length_descending(sample_list_2)
    print(f"\nOriginal List 2: {sample_list_2}")
    print(f"Sorted List 2: {result_2}")
    sample_list_3 = ["hello", "", "world", "a"]
    result_3 = sort_strings_by_length_descending(sample_list_3)
    print(f"\nOriginal List 3: {sample_list_3}")
    print(f"Sorted List 3: {result_3}")