import datetime
if __name__ == '__main__':
    input_date_str = "2023-10-27"
    try:
        date_object = datetime.datetime.strptime(input_date_str, "%Y-%m-%d").date()
        day_of_year = date_object.timetuple().tm_yday
        print(day_of_year)
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")