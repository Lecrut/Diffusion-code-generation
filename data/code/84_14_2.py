import datetime
def calculate_day_of_year(year, month, day):
    try:
        date_obj = datetime.date(year, month, day)
        return date_obj.timetuple().tm_yday
    except ValueError:
        return None
if __name__ == '__main__':
    year = 2023
    month = 10
    day = 27
    day_of_year = calculate_day_of_year(year, month, day)
    if day_of_year is not None:
        print(day_of_year)
    else:
        print("Invalid date entered.")