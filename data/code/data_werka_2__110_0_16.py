def sort_dates(date_list):
    if not date_list:
        return []
    return sorted(date_list, key=lambda d: tuple(int(p) for p in d.split('-')))

if __name__ == '__main__':
    dates = ['2023-10-01', '2021-05-15', '2022-01-01', '2023-01-01']
    result = sort_dates(dates)
    print(result)