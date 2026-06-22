import calendar

def find_weekday(year: int, month: int, day: int) -> str:
    if not (1 <= month <= 12):
        raise ValueError("Invalid month")
    if not (1 <= day <= 31):
        raise ValueError("Invalid day")
    
    try:
        weekday_num = calendar.weekday(year, month, day)
        return calendar.day_name[weekday_num]
    except ValueError:
        raise ValueError("Invalid date combination")

if __name__ == '__main__':
    print(find_weekday(2023, 12, 25))