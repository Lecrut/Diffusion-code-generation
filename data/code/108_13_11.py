from datetime import date

def is_valid_date(year, month, day):
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

def get_day_of_month():
    year = 2024
    month = 10
    day = 10
    if not is_valid_date(year, month, day):
        raise ValueError("Invalid date: October 10th, 2024")
    return date(year, month, day).day

if __name__ == '__main__':
    try:
        print(get_day_of_month())
    except ValueError as e:
        print(e)