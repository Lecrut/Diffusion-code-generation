from datetime import date, datetime

def sort_dates_descending(dates):
    return sorted(dates, reverse=True)

if __name__ == '__main__':
    sample_dates = [
        date(2023, 1, 15),
        date(2021, 5, 10),
        date(2024, 12, 31),
        date(2022, 8, 20),
    ]
    sorted_dates = sort_dates_descending(sample_dates)
    print(sorted_dates)