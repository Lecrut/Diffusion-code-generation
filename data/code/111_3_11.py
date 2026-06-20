from datetime import datetime, timedelta

def subtract_months(date_str, months):
    year, month, day = map(int, date_str.split('-'))
    try:
        new_date = datetime(year, month, day) - timedelta(days=months * 30)
        return new_date.strftime('%Y-%m-%d')
    except ValueError:
        return "Invalid date"

if __name__ == '__main__':
    result = subtract_months('2023-10-15', 3)
    print(result)