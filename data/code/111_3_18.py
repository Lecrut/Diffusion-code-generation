from datetime import datetime, timedelta

def subtract_months(year, month, day, months):
    if not (1 <= month <= 12) or not (1 <= day <= 31) or not isinstance(months, int):
        raise ValueError("Invalid input values")

    date = datetime(year, month, day)
    new_date = date - timedelta(days=months * 30)

    return new_date.year, new_date.month, new_date.day

if __name__ == '__main__':
    result = subtract_months(2023, 10, 15, 3)
    print(result)