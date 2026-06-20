def sort_date_strings(date_list):
    return sorted(date_list, key=lambda date: tuple(map(int, date.split('-'))))

if __name__ == '__main__':
    sample_dates = ['2023-04-01', '2022-01-15', '2023-03-20']
    sorted_dates = sort_date_strings(sample_dates)
    print(sorted_dates)