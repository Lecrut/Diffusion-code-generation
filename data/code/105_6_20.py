from datetime import date, timedelta

def next_multiple_of_7_days():
    start_date = date(2024, 1, 1)
    day_offset = 7
    next_date = start_date + timedelta(days=day_offset)
    return next_date

if __name__ == '__main__':
    result = next_multiple_of_7_days()
    print(result)