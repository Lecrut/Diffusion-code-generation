import datetime

def calculate_day_of_year(year, month, day):
    try:
        date_obj = datetime.date(year, month, day)
        return date_obj.timetuple().tm_yday
    except ValueError:
        return None

if __name__ == '__main__':
    year = 2023
    month = 11
    day = 15
    result = calculate_day_of_year(year, month, day)
    if result is not None:
        print(f"The day of the year for {year}-{month}-{day} is: {result}")
    else:
        print("Invalid date entered.")