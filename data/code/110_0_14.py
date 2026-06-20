def sort_date_strings(date_list):
    return sorted(date_list, key=lambda date: date)

if __name__ == '__main__':
    sample_dates = ['2023-04-01', '2022-12-25', '2023-01-01', '2023-03-15']
    sorted_dates = sort_date_strings(sample_dates)
    print(sorted_dates)