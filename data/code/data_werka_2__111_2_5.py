import datetime

def get_day_of_week(date_obj):
    return date_obj.strftime("%A")

if __name__ == '__main__':
    target_date = datetime.date(2024, 2, 29)
    day_name = get_day_of_week(target_date)
    print(day_name)