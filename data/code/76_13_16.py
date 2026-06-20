from datetime import date

def calculate_date_difference(date1: date, date2: date) -> int:
    return abs((date2 - date1).days)

if __name__ == '__main__':
    start_date = date(2023, 4, 5)
    end_date = date(2023, 6, 15)
    difference = calculate_date_difference(start_date, end_date)
    print(f"Difference between {start_date} and {end_date}: {difference} days")