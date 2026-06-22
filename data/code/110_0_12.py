def sort_dates_chronologically(date_strings):
    if not date_strings:
        return []
    return sorted(date_strings, key=lambda d: tuple(int(p) for p in d.split('-')))

if __name__ == '__main__':
    sample_dates = ['2024-02-29', '2020-01-01', '2023-12-25', '2021-07-04', '2022-11-11']
    sorted_result = sort_dates_chronologically(sample_dates)
    print(sorted_result)