from datetime import date

def get_date_difference(date1: date, date2: date) -> int:
    return abs((date2 - date1).days)

if __name__ == '__main__':
    date_a = date(2023, 1, 1)
    date_b = date(2023, 1, 10)
    difference = get_date_difference(date_a, date_b)
    print(f"Difference between {date_a} and {date_b}: {difference} days")