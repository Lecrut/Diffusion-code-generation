def sort_date_strings(date_list):
    return sorted(date_list, key=lambda date: date)

if __name__ == '__main__':
    sample_dates = ['2023-04-01', '2022-01-15', '2023-02-28']
    print(sort_date_strings(sample_dates))