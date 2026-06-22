def sort_date_strings(date_list):
    if not isinstance(date_list, list):
        raise ValueError("Input must be a list")
    for item in date_list:
        if not isinstance(item, str):
            raise ValueError("All items must be strings")
    return sorted(date_list, key=lambda x: x)

if __name__ == '__main__':
    unsorted_dates = ['2000-12-31', '1999-01-01', '2024-06-15', '2000-01-01']
    sorted_dates = sort_date_strings(unsorted_dates)
    print(sorted_dates)