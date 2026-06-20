from datetime import date

WEEKDAY_RANGE = range(0, 5)

def is_weekday(date_obj: date) -> bool:
    return date_obj.weekday() in WEEKDAY_RANGE

if __name__ == '__main__':
    date1 = date(2023, 10, 2)
    date2 = date(2023, 10, 7)
    print(f"Is {date1} a weekday? {is_weekday(date1)}")
    print(f"Is {date2} a weekday? {is_weekday(date2)}")