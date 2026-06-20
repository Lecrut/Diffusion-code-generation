from datetime import datetime, timedelta

def add_30_days_to_july_fourth():
    july_fourth = datetime(2024, 7, 4)
    new_date = july_fourth + timedelta(days=30)
    return new_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    print(add_30_days_to_july_fourth())