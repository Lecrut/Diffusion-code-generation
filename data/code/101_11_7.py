from datetime import date

def validate_date(year: int, month: int, day: int) -> bool:
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

def determine_weekday(year: int, month: int, day: int) -> str:
    if not validate_date(year, month, day):
        raise ValueError("Invalid date")
    
    weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekday_names[date(year, month, day).weekday()]

if __name__ == '__main__':
    year = 2023
    month = 10
    day = 10
    print(determine_weekday(year, month, day))