from datetime import date

def get_day_of_month(year=2024, month=10, day=10):
    try:
        return date(year, month, day).day
    except ValueError as e:
        raise ValueError(f"Invalid date: {e}")

if __name__ == '__main__':
    print(get_day_of_month())