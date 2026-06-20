from datetime import datetime

def prepend_day_name(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"{result.strftime('%A')} {result}"
    return wrapper

@prepend_day_name
def get_current_date():
    return datetime.now()

if __name__ == '__main__':
    print(get_current_date())