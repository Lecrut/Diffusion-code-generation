from datetime import datetime, timedelta

def subtract_three_months(year, month, day):
    date = datetime(year, month, day)
    new_date = date - timedelta(days=3 * 30)
    return (new_date.year, new_date.month, new_date.day)
if __name__ == '__main__':
    year, month, day = subtract_three_months(2023, 10, 15)
    print(year, month, day)