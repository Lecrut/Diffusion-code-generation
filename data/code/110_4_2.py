def sort_date_tuples(dates):
    return sorted(dates)

if __name__ == '__main__':
    sample_dates = [
        (2023, 10, 15),
        (2021, 5, 1),
        (2023, 1, 1),
        (2020, 12, 31),
        (2023, 10, 14)
    ]
    sorted_dates = sort_date_tuples(sample_dates)
    print(sorted_dates)