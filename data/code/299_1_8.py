import datetime

def is_weekend(date_obj):
    weekday = date_obj.weekday()
    return weekday >= 5

if __name__ == '__main__':
    sample_date_str = '2023-10-07'
    sample_date_obj = datetime.datetime.strptime(sample_date_str, '%Y-%m-%d').date()
    print(f"Is {sample_date_str} a weekend? {is_weekend(sample_date_obj)}")