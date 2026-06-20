WEEK_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_since_epoch(year: int, month: int, day: int) -> int:
    days = 0
    for y in range(2000, year):
        days += 366 if is_leap_year(y) else 365
    months = [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for m in range(month - 1):
        days += months[m]
    days += day
    return days

def get_day_of_week(year: int, month: int, day: int) -> str:
    epoch = (2000, 1, 1)
    days_diff = days_since_epoch(year, month, day) - days_since_epoch(*epoch)
    day_index = (days_diff + 5) % 7
    return WEEK_DAYS[day_index]

if __name__ == '__main__':
    print(f"Date: 2024-02-29, Day of Week: {get_day_of_week(2024, 2, 29)}")