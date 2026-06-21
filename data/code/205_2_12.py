def sort_strings(string_list):
    return sorted(string_list, key=str.lower)

if __name__ == '__main__':
    sample_list = ["banana", "Apple", "cherry", "date"]
    sorted_list = sort_strings(sample_list)
    print(sorted_list)