from datetime import date

def is_valid_date(year: int, month: int, day: int) -> bool:
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

def determine_weekday(year: int, month: int, day: int) -> str:
    if not is_valid_date(year, month, day):
        raise ValueError("Invalid date")
    
    weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekday_names[date(year, month, day).weekday()]

if __name__ == '__main__':
    print(determine_weekday(2023, 10, 10))