def sort_dates(date_list):
    return sorted(date_list)

if __name__ == '__main__':
    dates = [
        (2023, 10, 15),
        (2021, 5, 20),
        (2023, 1, 1),
        (2020, 12, 31),
        (2022, 7, 10)
    ]
    sorted_dates = sort_dates(dates)
    print(sorted_dates)