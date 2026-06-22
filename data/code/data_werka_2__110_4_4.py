def sort_date_tuples(dates):
    return sorted(dates)

if __name__ == '__main__':
    sample_dates = [
        (2023, 1, 15),
        (2021, 12, 31),
        (2022, 6, 1),
        (2020, 2, 29),
        (2023, 1, 10)
    ]
    sorted_dates = sort_date_tuples(sample_dates)
    print(sorted_dates)