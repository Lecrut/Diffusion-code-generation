import datetime

def prepend_day_name(func):
    def wrapper(*args, **kwargs):
        date_obj = func(*args, **kwargs)
        day_name = date_obj.strftime('%A')
        return f"{day_name} {date_obj}"
    return wrapper

@prepend_day_name
def get_current_date():
    return datetime.datetime.now().date()

if __name__ == '__main__':
    print(get_current_date())