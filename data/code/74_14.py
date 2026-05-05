import datetime
def calculate_day_of_week(date_string):
    try:
        date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        day_of_week = date_object.strftime("%A")
        return day_of_week
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."
if __name__ == '__main__':
    sample_date = "2023-10-27"
    result = calculate_day_of_week(sample_date)
    print(result)