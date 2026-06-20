MONTHS_PER_YEAR = 12

def sort_date_tuples(date_list):
    return sorted(date_list, key=lambda date: (date[0], date[1] * MONTHS_PER_YEAR + date[2]))
if __name__ == '__main__':
    sample_dates = [(2023, 4, 5), (2022, 1, 1), (2023, 1, 15)]
    sorted_dates = sort_date_tuples(sample_dates)
    print(sorted_dates)