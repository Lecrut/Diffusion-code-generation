def sort_strings_by_length_descending(string_list):
    return sorted(string_list, key=len, reverse=True)
if __name__ == '__main__':
    sample_list_1 = ["apple", "banana", "kiwi", "orange", "grapefruit"]
    sample_list_2 = ["a", "bb", "ccc", "dddd", "eeeee"]
    sample_list_3 = []
    sample_list_4 = ["long", "short", "medium", "longer"]
    result_1 = sort_strings_by_length_descending(sample_list_1)
    print(f"Sample 1 Input: {sample_list_1}")
    print(f"Sample 1 Output: {result_1}\n")
    result_2 = sort_strings_by_length_descending(sample_list_2)
    print(f"Sample 2 Input: {sample_list_2}")
    print(f"Sample 2 Output: {result_2}\n")
    result_3 = sort_strings_by_length_descending(sample_list_3)
    print(f"Sample 3 Input: {sample_list_3}")
    print(f"Sample 3 Output: {result_3}\n")
    result_4 = sort_strings_by_length_descending(sample_list_4)
    print(f"Sample 4 Input: {sample_list_4}")
    print(f"Sample 4 Output: {result_4}\n")