import datetime

DAY_NAMES = {
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
        day_name = DAY_NAMES[date_obj.weekday()]
        return f"{day_name} {date_obj}"
    return wrapper

@prepend_day_name
def get_current_date():
    return datetime.datetime.now()

if __name__ == '__main__':
    print(get_current_date())