def sort_dates(date_strings):
    return sorted(date_strings, key=lambda d: d)

if __name__ == '__main__':
    dates = ['2023-10-15', '2021-01-01', '2022-05-20', '2023-01-01']
    result = sort_dates(dates)
    print(result)