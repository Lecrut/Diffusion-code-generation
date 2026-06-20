import datetime

def prepend_day_name(func):
    def wrapper(*args, **kwargs):
        date_obj = func(*args, **kwargs)
        day_name = date_obj.strftime('%A')
        return f"{day_name} {date_obj}"
    return wrapper

@prepend_day_name
def get_current_date():
    return datetime.date.today()

if __name__ == '__main__':
    sample_date_monday = datetime.date(2023, 10, 23)
    result_monday = get_current_date()
    print(f"Day and date for Monday: {result_monday}")
    
    sample_date_saturday = datetime.date(2023, 10, 28)
    result_saturday = get_current_date()
    print(f"Day and date for Saturday: {result_saturday}")