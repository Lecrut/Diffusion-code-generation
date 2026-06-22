def sort_dates_ascending(date_strings):
    if not date_strings:
        return []
    return sorted(date_strings, key=lambda x: (int(x[0:4]), int(x[5:7]), int(x[8:10])))

if __name__ == '__main__':
    unsorted_dates = ['2020-01-12', '2023-11-01', '2019-05-30', '2023-11-01', '2021-02-28']
    sorted_output = sort_dates_ascending(unsorted_dates)
    print(sorted_output)