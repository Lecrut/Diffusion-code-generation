def sort_strings_desc(strings):
    return sorted(strings, reverse=True)

if __name__ == '__main__':
    sample_values = ["grape", "apple", "orange"]
    sorted_list = sort_strings_desc(sample_values)
    print(sorted_list)