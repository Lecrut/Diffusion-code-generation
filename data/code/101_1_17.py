import calendar

WEEKDAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def get_weekday_name(year, month, day):
    _, weekday_index = calendar.monthrange(year, month)
    return WEEKDAY_NAMES[weekday_index]

if __name__ == '__main__':
    print(get_weekday_name(2023, 10, 26))
    print(get_weekday_name(2024, 1, 1))
    print(get_weekday_name(2025, 12, 31))