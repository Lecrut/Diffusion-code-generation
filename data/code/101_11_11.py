from datetime import date

WEEKDAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def determine_weekday(year, month, day) -> str:
    date_obj = date(year, month, day)
    return WEEKDAY_NAMES[date_obj.weekday()]

if __name__ == '__main__':
    print(determine_weekday(2023, 10, 10))