from datetime import date

def sort_dates(dates):
    return sorted(dates)

if __name__ == '__main__':
    dates = [date(2023, 10, 1), date(2021, 5, 15), date(2022, 1, 1)]
    print(sort_dates(dates))