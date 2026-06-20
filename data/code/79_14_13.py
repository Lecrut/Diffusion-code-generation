import datetime

def first_day_next_month(date_obj):
    return (date_obj.replace(day=28) + datetime.timedelta(days=4)).replace(day=1)

if __name__ == '__main__':
    sample_date = datetime.datetime(2024, 3, 31)
    result = first_day_next_month(sample_date).strftime('%Y-%m-%d')
    print(result)