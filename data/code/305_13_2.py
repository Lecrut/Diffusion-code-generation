def sort_dates(date_list):
    return sorted(date_list)
if __name__ == '__main__':
    unsorted_dates = ["2023-10-26", "2023-01-01", "2024-05-15", "2023-07-30"]
    sorted_dates = sort_dates(unsorted_dates)
    print(sorted_dates)