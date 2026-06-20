from datetime import datetime, timedelta

def first_day_of_next_month(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    next_month = date_obj.replace(day=1) + timedelta(days=32)
    return next_month.replace(day=1).strftime('%Y-%m-%d')

if __name__ == '__main__':
    sample_date_str = "2023-11-25"
    result = first_day_of_next_month(sample_date_str)
    print(result)