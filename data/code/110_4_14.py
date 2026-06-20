def sort_date_tuples(date_list):
    return sorted(date_list)

if __name__ == '__main__':
    sample_dates = [(2023, 4, 5), (2022, 1, 15), (2023, 1, 1)]
    print(sort_date_tuples(sample_dates))