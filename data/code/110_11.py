def sort_dates(date_strings):
    return sorted(date_strings)
if __name__ == '__main__':
    sample_dates = ["2023-01-15", "2022-12-31", "2023-05-20", "2022-11-01"]
    sorted_dates = sort_dates(sample_dates)
    print(sorted_dates)