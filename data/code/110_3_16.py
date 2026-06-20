from datetime import date

def sort_dates(dates):
    return sorted(dates)

if __name__ == '__main__':
    dates = [date(2023, 1, 1), date(2022, 12, 31), date(2023, 2, 15)]
    sorted_dates = sort_dates(dates)
    print(sorted_dates)