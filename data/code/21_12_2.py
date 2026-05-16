import operator
def sort_strings_case_insensitive(string_list):
    return sorted(string_list, key=str.lower)
if __name__ == '__main__':
    sample_list = ["Apple", "banana", "Cherry", "date", "elderberry"]
    sorted_list = sort_strings_case_insensitive(sample_list)
    print(sorted_list)