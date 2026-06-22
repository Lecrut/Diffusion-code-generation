from datetime import date

def is_weekend(year, month, day):
    try:
        target_date = date(year, month, day)
        return target_date.weekday() >= 5
    except ValueError as e:
        print(f"Invalid date: {e}")
        return False

if __name__ == '__main__':
    print(is_weekend(2023, 10, 7))
    print(is_weekend(2023, 10, 8))
    print(is_weekend(2023, 10, 9))