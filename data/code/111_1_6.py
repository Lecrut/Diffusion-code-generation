import datetime

def add_30_days_to_date(date_obj):
    return date_obj + datetime.timedelta(days=30)

if __name__ == '__main__':
    date1 = datetime.date(2024, 7, 4)
    result1 = add_30_days_to_date(date1)
    print(f"Original: {date1}, Result: {result1}")