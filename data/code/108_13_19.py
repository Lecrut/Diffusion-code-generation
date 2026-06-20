from datetime import date

def validate_date(year, month, day):
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

def get_day_of_month(year=2024, month=10, day=10):
    if not validate_date(year, month, day):
        raise ValueError("Invalid date.")
    return date(year, month, day).day

if __name__ == '__main__':
    print(get_day_of_month())