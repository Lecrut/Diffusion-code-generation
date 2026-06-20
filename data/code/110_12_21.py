def sort_date_tuples(date_list):
    return sorted(date_list, key=lambda date: (date[0], date[1], date[2]))

if __name__ == '__main__':
    sample_dates = [(2023, 4, 15), (2022, 1, 1), (2023, 3, 20)]
    sorted_dates = sort_date_tuples(sample_dates)
    print(sorted_dates)