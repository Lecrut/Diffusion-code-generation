from datetime import date

WEEKDAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def determine_weekday(year, month, day) -> str:
    return WEEKDAY_NAMES[date(year, month, day).weekday()]

if __name__ == '__main__':
    print(determine_weekday(2023, 10, 10))