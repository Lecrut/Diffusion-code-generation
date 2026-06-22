from datetime import date, datetime

def sort_dates_descending(dates: list[date]) -> list[date]:
    return sorted(dates, reverse=True)

if __name__ == '__main__':
    sample_dates = [
        date(2023, 1, 15),
        date(2021, 12, 31),
        date(2024, 6, 1),
        date(2022, 3, 10),
    ]
    result = sort_dates_descending(sample_dates)
    print(result)