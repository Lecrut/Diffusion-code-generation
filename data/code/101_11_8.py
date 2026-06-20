from datetime import date

def get_day_of_week(year: int, month: int, day: int) -> str:
    weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekday_names[date(year, month, day).weekday()]

if __name__ == '__main__':
    print(get_day_of_week(2023, 10, 10))