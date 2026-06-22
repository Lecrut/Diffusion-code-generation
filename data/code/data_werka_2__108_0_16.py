import datetime

def calculate_day_component(date_instance):
    year_part = date_instance.year
    month_part = date_instance.month
    day_part = date_instance.day
    return day_part

if __name__ == '__main__':
    target_date = datetime.date(1995, 11, 22)
    computed_day = calculate_day_component(target_date)
    print(computed_day)