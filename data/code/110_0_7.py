def sort_date_strings(date_list):
    return sorted(date_list, key=lambda date: (int(date[:4]), int(date[5:7]), int(date[8:])))

if __name__ == '__main__':
    sample_dates = ['2023-04-01', '2022-01-15', '2023-03-20']
    sorted_dates = sort_date_strings(sample_dates)
    print(sorted_dates)