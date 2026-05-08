def sort_dates(date_list):
    return sorted(date_list)
if __name__ == '__main__':
    dates = ["2023-01-15", "2023-01-01", "2023-01-15", "2023-02-20"]
    sorted_dates = sort_dates(dates)
    print(sorted_dates)