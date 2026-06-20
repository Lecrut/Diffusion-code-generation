import datetime

def add_30_days(date_obj):
    return date_obj + datetime.timedelta(days=30)

if __name__ == '__main__':
    original_date = datetime.date(2024, 7, 4)
    result_date = add_30_days(original_date)
    print(f"Original: {original_date}, Result: {result_date}")