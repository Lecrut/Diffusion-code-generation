import datetime

def get_january_first_weekday(year):
    if year < 1:
        raise ValueError("Year must be a positive integer")
    target_date = datetime.date(year, 1, 1)
    return target_date.strftime("%A")

if __name__ == '__main__':
    target_year = 2024
    day_name = get_january_first_weekday(target_year)
    print(day_name)