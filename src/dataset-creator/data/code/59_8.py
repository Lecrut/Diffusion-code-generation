from datetime import date
def get_day_of_week(year: int, month: int, day: int) -> str:
    d = date(year, month, day)
    return d.strftime("%A")
if __name__ == '__main__':
    print(get_day_of_week(2023, 10, 5))