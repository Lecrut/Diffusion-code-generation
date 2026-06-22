def sort_date_tuples(dates):
    return sorted(dates, key=lambda d: (d[0], d[1], d[2]))

if __name__ == '__main__':
    sample_dates = [
        (2023, 1, 15),
        (2021, 12, 31),
        (2022, 6, 1),
        (2023, 1, 1),
        (2021, 1, 1)
    ]
    sorted_dates = sort_date_tuples(sample_dates)
    print(sorted_dates)