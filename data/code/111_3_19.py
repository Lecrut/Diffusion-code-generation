from datetime import datetime, timedelta

def subtract_months(date_str, months):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    new_date_obj = date_obj - timedelta(days=months * 30)
    return new_date_obj.strftime('%Y-%m-%d')
if __name__ == '__main__':
    result = subtract_months('2023-10-15', 3)
    print(result)