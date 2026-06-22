def sort_dates(date_strings):
    return sorted(date_strings, key=lambda d: d)

if __name__ == '__main__':
    dates = ['2023-10-01', '2021-05-15', '2022-12-31', '2020-01-01']
    result = sort_dates(dates)
    print(result)