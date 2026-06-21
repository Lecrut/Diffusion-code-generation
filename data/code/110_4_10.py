def sort_date_tuples(dates):
    return sorted(dates)

if __name__ == '__main__':
    sample_dates = [(2023, 10, 15), (2021, 5, 1), (2022, 12, 31), (2021, 5, 2)]
    result = sort_date_tuples(sample_dates)
    print(result)