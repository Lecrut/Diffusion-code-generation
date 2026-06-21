def sort_list_case_insensitive(input_list):
    return sorted(input_list, key=str.lower)

if __name__ == '__main__':
    sample_values = ["banana", "Apple", "cherry", "date"]
    result = sort_list_case_insensitive(sample_values)
    print(result)