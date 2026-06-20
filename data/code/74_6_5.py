from datetime import datetime

def prepend_day_name(func):
    def wrapper(date_obj):
        day_name = date_obj.strftime('%A')
        return f"{day_name}, {date_obj}"
    return wrapper

@prepend_day_name
def format_date(date_obj):
    return date_obj

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5)
    print(format_date(sample_date))