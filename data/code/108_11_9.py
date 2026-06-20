import datetime

def get_day_of_month(date_obj):
    try:
        return date_obj.day
    except AttributeError:
        return None

if __name__ == '__main__':
    sample_date = datetime.date(2023, 3, 15)
    print(f"Day of month for {sample_date}: {get_day_of_month(sample_date)}")