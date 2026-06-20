from datetime import date

def is_valid_date(year: int, month: int, day: int) -> bool:
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

def get_day_of_month(year: int = 2024, month: int = 10, day: int = 10) -> int:
    if not is_valid_date(year, month, day):
        raise ValueError("Invalid date")
    return date(year, month, day).day

if __name__ == '__main__':
    print(get_day_of_month())