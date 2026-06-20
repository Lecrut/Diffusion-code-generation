import datetime

def get_first_day_next_month(date_obj):
    try:
        return (date_obj.replace(day=28) + datetime.timedelta(days=4)).replace(day=1)
    except Exception as e:
        raise ValueError("Error: Invalid date object.") from e

if __name__ == '__main__':
    sample_date = datetime.datetime(2024, 3, 31)
    result = get_first_day_next_month(sample_date)
    print(result.strftime('%Y-%m-%d'))