from datetime import date

WEEKDAY_START = 0
WEEKDAY_END = 4

def is_business_day(target: date) -> bool:
    day_index = target.weekday()
    return WEEKDAY_START <= day_index <= WEEKDAY_END

if __name__ == '__main__':
    monday = date(2023, 10, 23)
    saturday = date(2023, 10, 28)
    sunday = date(2023, 10, 29)
    print(is_business_day(monday))
    print(is_business_day(saturday))
    print(is_business_day(sunday))