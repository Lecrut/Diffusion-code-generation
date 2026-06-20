from datetime import datetime

def day_of_week_first_of_month(date_str):
    year, month, _ = map(int, date_str.split('-'))
    first_day = datetime(year, month, 1)
    return first_day.weekday()

if __name__ == '__main__':
    sample_date = '2023-04-15'
    print(day_of_week_first_of_month(sample_date))