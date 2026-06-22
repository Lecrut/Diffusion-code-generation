def sort_dates(dates):
    return sorted(dates)

if __name__ == '__main__':
    sample_dates = [
        (2023, 10, 5),
        (2021, 1, 1),
        (2022, 12, 31),
        (2023, 1, 1),
        (2021, 1, 1)
    ]
    sorted_dates = sort_dates(sample_dates)
    print(sorted_dates)