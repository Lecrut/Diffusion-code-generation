def sort_date_strings(date_list):
    return sorted(date_list, key=lambda date: (int(date[:4]), int(date[5:7]), int(date[8:])))

if __name__ == '__main__':
    sample_dates = ['2023-01-15', '2022-12-25', '2023-01-01']
    sorted_dates = sort_date_strings(sample_dates)
    print(sorted_dates)