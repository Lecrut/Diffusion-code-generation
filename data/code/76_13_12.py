from datetime import date

def days_between(date1: date, date2: date) -> int:
    return abs((date2 - date1).days)

if __name__ == '__main__':
    start_date = date(2023, 4, 1)
    end_date = date(2023, 5, 15)
    difference = days_between(start_date, end_date)
    print(f"Days between {start_date} and {end_date}: {difference}")