import datetime

DAY_NAME_MAP = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

def prepend_day_name(func):
    def wrapper(*args, **kwargs):
        date_obj = func(*args, **kwargs)
        day_name = DAY_NAME_MAP[date_obj.weekday()]
        return f"{day_name} {date_obj.strftime('%Y-%m-%d')}"
    return wrapper

@prepend_day_name
def get_current_date():
    return datetime.date.today()

if __name__ == '__main__':
    current_date = get_current_date()
    print(f"Current date with day name: {current_date}")