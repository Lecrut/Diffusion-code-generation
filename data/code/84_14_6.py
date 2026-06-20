import datetime

def calculate_day_of_year(year, month, day):
    try:
        date_obj = datetime.date(year, month, day)
        return date_obj.timetuple().tm_yday
    except ValueError as e:
        raise ValueError("Invalid date entered: " + str(e))

if __name__ == '__main__':
    year = 2023
    month = 10
    day = 27
    try:
        day_of_year = calculate_day_of_year(year, month, day)
        print(f"The day of the year for {year}-{month}-{day} is: {day_of_year}")
    except ValueError as e:
        print(e)