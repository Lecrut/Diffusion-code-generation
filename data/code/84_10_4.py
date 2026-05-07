import datetime
def calculate_day_of_year(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
        day_of_year = date_obj.timetuple().tm_yday
        return day_of_year
    except ValueError:
        return "Invalid date format"
if __name__ == '__main__':
    sample_date = "2023-10-27"
    day_num = calculate_day_of_year(sample_date)
    print(day_num)