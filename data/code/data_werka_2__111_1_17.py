from datetime import date, timedelta

def add_days_to_date(year, month, day, num_days):
    base_date = date(year, month, day)
    result_date = base_date + timedelta(days=num_days)
    return result_date.strftime("%Y-%m-%d")

if __name__ == '__main__':
    print(add_days_to_date(2024, 7, 4, 30))