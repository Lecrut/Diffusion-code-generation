import datetime as dt
def get_day_of_week(year: int, month: int, day: int) -> str:
    return dt.date(year, month, day).strftime("%A")
if __name__ == '__main__':
    print(get_day_of_week(2023, 10, 5))