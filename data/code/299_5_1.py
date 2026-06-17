from datetime import date
def is_weekend(dt: date) -> bool:
    day_of_week = dt.weekday()
    return day_of_week >= 5
if __name__ == '__main__':
    date1 = date(2023, 10, 1)
    date2 = date(2023, 10, 7)
    date3 = date(2023, 10, 8)
    date4 = date(2023, 10, 15)
    print(f"Is {date1} a weekend? {is_weekend(date1)}")
    print(f"Is {date2} a weekend? {is_weekend(date2)}")
    print(f"Is {date3} a weekend? {is_weekend(date3)}")
    print(f"Is {date4} a weekend? {is_weekend(date4)}")