import datetime

def add_30_days(date_obj):
    new_date = date_obj + datetime.timedelta(days=30)
    return new_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    target_date = datetime.date(2024, 7, 4)
    result_date = add_30_days(target_date)
    print(result_date)