def sort_strings_case_insensitive(strings):
    return sorted(strings, key=str.lower)
if __name__ == '__main__':
    data = ["banana", "Apple", "cherry", "apple", "DATE"]
    result = sort_strings_case_insensitive(data)
    for item in result:
        print(item)