import datetime

def check_is_weekday(date_string):
    parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    day_of_week = parsed_date.weekday()
    is_week = day_of_week < 5
    return is_week

if __name__ == '__main__':
    target_dates = ["2024-02-14", "2024-02-15", "2024-02-16"]
    for date_str in target_dates:
        result = check_is_weekday(date_str)
        print(result)