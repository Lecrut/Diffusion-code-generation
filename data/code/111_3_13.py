from datetime import datetime, timedelta

def subtract_three_months(date):
    year = date.year - (date.month <= 3)
    month = (date.month - 1) % 12 + 1
    day = min(date.day, [31, 28 + (year % 4 == 0 and year % 100 != 0 or year % 400 == 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1])
    return datetime(year, month, day)

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 15)
    result_date = subtract_three_months(sample_date)
    print(result_date.strftime('%Y-%m-%d'))