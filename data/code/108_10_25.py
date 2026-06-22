import datetime

def get_january_1st_weekday(year):
    target_date = datetime.date(year, 1, 1)
    return target_date.strftime("%A")

if __name__ == '__main__':
    year_value = 2024
    weekday_name = get_january_1st_weekday(year_value)
    print(weekday_name)