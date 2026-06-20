from datetime import date

def sort_dates(dates):
    return sorted(dates)

if __name__ == '__main__':
    sample_dates = [date(2023, 1, 5), date(2022, 12, 25), date(2023, 1, 1)]
    print(sort_dates(sample_dates))