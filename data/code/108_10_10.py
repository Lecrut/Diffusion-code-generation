import datetime

def get_january_first_day(year):
    if year < 1:
        raise ValueError("Year must be a positive integer")
    first_day = datetime.date(year, 1, 1)
    return first_day.strftime("%A")

if __name__ == '__main__':
    target_year = 2024
    day_name = get_january_first_day(target_year)
    print(day_name)