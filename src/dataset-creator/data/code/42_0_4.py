def sort_strings_case_insensitive(strings):
    return sorted(strings, key=str.lower)
if __name__ == '__main__':
    data = ["Banana", "apple", "Cherry", "date", "APPLE"]
    sorted_data = sort_strings_case_insensitive(data)
    for item in sorted_data:
        print(item)