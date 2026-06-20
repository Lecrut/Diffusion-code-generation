import datetime

def prepend_day_name(func):

    def wrapper(*args, **kwargs):
        date_obj = func(*args, **kwargs)
        day_name = date_obj.strftime('%A')
        return f'{day_name} {date_obj}'
    return wrapper

@prepend_day_name
def get_current_date():
    return datetime.date.today()
if __name__ == '__main__':
    sample_date_1 = datetime.date(2023, 10, 23)
    sample_date_2 = datetime.date(2023, 10, 28)
    print(get_current_date())
    print(f'Day of week for {sample_date_1}: {get_current_date()}')
    print(f'Day of week for {sample_date_2}: {get_current_date()}')