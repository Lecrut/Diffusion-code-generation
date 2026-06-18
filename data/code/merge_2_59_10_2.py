import datetime
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def calculate_day_of_week(date_str, format='%Y-%m-%d'):
    try:
        date_obj = datetime.datetime.strptime(date_str, format)
        return date_obj.strftime('%A')
    except ValueError as e:
        raise ValueError(f"Invalid date format or invalid date. Error details: {e}")
if __name__ == '__main__':
    sample_dates = [
        "2023-10-05",
        "2024-02-29",
        "2023-02-28"
    ]
    for date in sample_dates:
        try:
            day_name = calculate_day_of_week(date)
            print(f"{date} is a {day_name}")
        except ValueError as ve:
            print(f"Error processing '{date}': {ve}")