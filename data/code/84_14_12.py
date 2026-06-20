import datetime

def calculate_day_of_year(year, month, day):
    try:
        date_obj = datetime.date(year, month, day)
        return date_obj.timetuple().tm_yday
    except ValueError:
        return None

if __name__ == '__main__':
    YEAR = 2023
    MONTH = 10
    DAY = 27
    day_of_year = calculate_day_of_year(YEAR, MONTH, DAY)
    if day_of_year is not None:
        print(f"The day of the year for {YEAR}-{MONTH}-{DAY} is: {day_of_year}")
    else:
        print("Invalid date entered.")