from datetime import datetime

DAY_OF_MONTH = 'day'

def get_day_of_month(date_obj: datetime) -> int:
    return getattr(date_obj, DAY_OF_MONTH)

if __name__ == '__main__':
    sample_date = datetime(2023, 9, 15)
    print(get_day_of_month(sample_date))