import datetime

def is_valid_date(year, month, day):
    try:
        datetime.date(year, month, day)
        return True
    except ValueError:
        return False

def calculate_day_of_year(year, month, day):
    if not is_valid_date(year, month, day):
        raise ValueError("Invalid date entered.")
    date_obj = datetime.date(year, month, day)
    return date_obj.timetuple().tm_yday

if __name__ == '__main__':
    year = 2023
    month = 10
    day = 5
    try:
        day_of_year = calculate_day_of_year(year, month, day)
        print(f"The day of the year for {year}-{month}-{day} is: {day_of_year}")
    except ValueError as e:
        print(e)