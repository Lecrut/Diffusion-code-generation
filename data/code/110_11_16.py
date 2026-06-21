import datetime

def sort_datetimes(dates: list[datetime.datetime]) -> list[datetime.datetime]:
    return sorted(dates)

if __name__ == '__main__':
    sample_dates = [
        datetime.datetime(2023, 10, 15, 10, 30),
        datetime.datetime(2021, 5, 20, 8, 0),
        datetime.datetime(2024, 1, 1, 0, 0),
        datetime.datetime(2022, 12, 31, 23, 59),
    ]
    result = sort_datetimes(sample_dates)
    print(result)