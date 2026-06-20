import datetime

def prepend_day_name(func):
    def wrapper(*args, **kwargs):
        date_obj = func(*args, **kwargs)
        return f"{date_obj.strftime('%A')} {date_obj}"
    return wrapper

@prepend_day_name
def get_current_date():
    return datetime.datetime.now().date()

if __name__ == '__main__':
    print(get_current_date())