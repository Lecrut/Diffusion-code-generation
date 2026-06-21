def filter_names_by_initial(names, initial):
    return [name for name in names if name.startswith(initial)]

if __name__ == '__main__':
    sample_names = ["Alex", "Brian", "Cindy", "David", "Ella"]
    initial_char = 'A'
    filtered_list = filter_names_by_initial(sample_names, initial_char)
    print(filtered_list)