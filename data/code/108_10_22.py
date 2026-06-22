import datetime

def get_january_first_weekday(year):
    if not isinstance(year, int):
        raise ValueError("Year must be an integer")
    if year < 1:
        raise ValueError("Year must be positive")
    date_instance = datetime.date(year, 1, 1)
    return date_instance.strftime("%A")

if __name__ == '__main__':
    target_year = 2024
    weekday_name = get_january_first_weekday(target_year)
    print(weekday_name)