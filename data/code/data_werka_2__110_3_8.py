from datetime import date

def sort_dates(dates):
    return sorted(dates)

if __name__ == '__main__':
    dates = [date(2023, 1, 15), date(2021, 5, 10), date(2022, 12, 25), date(2020, 3, 1)]
    result = sort_dates(dates)
    print(result)