def alphabetize_strings(string_list):
    return sorted(string_list)

if __name__ == '__main__':
    unsorted_items = ["grape", "apple", "cherry", "date", "elderberry"]
    organized_items = alphabetize_strings(unsorted_items)
    print(organized_items)