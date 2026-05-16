import datetime
def calculate_day_of_year(year, month, day):
    try:
        date_obj = datetime.date(year, month, day)
        day_of_year = date_obj.timetuple().tm_yday
        return day_of_year
    except ValueError:
        return "Invalid date"
if __name__ == '__main__':
    year = 2024
    month = 2
    day = 29
    result = calculate_day_of_year(year, month, day)
    print(result)