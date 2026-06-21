from datetime import date, timedelta

def add_days_to_july_4():
    start_date = date(2024, 7, 4)
    delta = timedelta(days=30)
    result_date = start_date + delta
    return result_date.strftime("%Y-%m-%d")

if __name__ == '__main__':
    print(add_days_to_july_4())