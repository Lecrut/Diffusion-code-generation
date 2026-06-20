from datetime import datetime, timedelta

def add_30_days_to_july_4():
    date_obj = datetime(2024, 7, 4)
    new_date_obj = date_obj + timedelta(days=30)
    return new_date_obj.strftime('%Y-%m-%d')

if __name__ == '__main__':
    print(add_30_days_to_july_4())