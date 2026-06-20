import datetime

def add_days_to_date(date_obj, days):
    return date_obj + datetime.timedelta(days=days)

if __name__ == '__main__':
    sample_date = datetime.date(2024, 7, 4)
    result_date = add_days_to_date(sample_date, 30)
    print(f"Original: {sample_date}, Result: {result_date}")