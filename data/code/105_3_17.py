from datetime import date

def next_15th_day_of_month(start_date):
    year = start_date.year
    month = start_date.month + 1
    if month > 12:
        year += 1
        month = 1
    target_date = date(year, month, 1) + timedelta(days=14)
    return target_date

if __name__ == '__main__':
    sample_date = date(2023, 3, 3)
    result = next_15th_day_of_month(sample_date)
    print(result)