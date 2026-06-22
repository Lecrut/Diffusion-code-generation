import datetime

def get_day_of_week(year: int, month: int, day: int) -> str:
    date_obj = datetime.date(year, month, day)
    return date_obj.strftime("%A")

if __name__ == '__main__':
    result = get_day_of_week(2025, 3, 15)
    print(result)