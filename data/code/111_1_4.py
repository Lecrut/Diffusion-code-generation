from datetime import datetime, timedelta

def add_30_days_to_july_4():
    july_4 = datetime(2024, 7, 4)
    result_date = july_4 + timedelta(days=30)
    return result_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    print(add_30_days_to_july_4())