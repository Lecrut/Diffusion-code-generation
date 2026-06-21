import datetime

def get_weekday_for_date(year, month, day):
    date_instance = datetime.date(year, month, day)
    full_weekday_name = date_instance.strftime("%A")
    return full_weekday_name.upper()

if __name__ == '__main__':
    target_year = 2024
    target_month = 7
    target_day = 4
    computed_weekday = get_weekday_for_date(target_year, target_month, target_day)
    print(computed_weekday)