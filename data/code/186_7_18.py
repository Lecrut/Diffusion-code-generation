def sort_numeric_strings(string_list):
    try:
        return sorted(string_list, key=int)
    except ValueError as e:
        raise ValueError("All elements must be convertible to integers") from e

if __name__ == '__main__':
    sample_list = ["3", "15", "7", "2"]
    print("Original list:", sample_list)
    sorted_list = sort_numeric_strings(sample_list)
    print("Sorted list by integer value:", sorted_list)