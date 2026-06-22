from datetime import date

def sort_dates(dates):
    return sorted(dates)

if __name__ == '__main__':
    dates = [date(2023, 1, 15), date(2020, 5, 1), date(2021, 12, 25)]
    print(sort_dates(dates))