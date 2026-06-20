import datetime

def add_30_days(date_obj):
    try:
        return date_obj + datetime.timedelta(days=30)
    except Exception as e:
        raise ValueError(f"Invalid date: {e}")

if __name__ == '__main__':
    date1 = datetime.date(2024, 7, 4)
    result1 = add_30_days(date1)
    print(result1.strftime("%Y-%m-%d"))