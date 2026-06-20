import datetime

def get_day_of_week(date_string):
    date_format = "%Y-%m-%d"
    try:
        date_obj = datetime.datetime.strptime(date_string, date_format)
        return date_obj.strftime("%A")
    except ValueError:
        raise ValueError(f"Could not parse date string: {date_string}")

if __name__ == '__main__':
    test_date = "2024-01-01"
    print(get_day_of_week(test_date))