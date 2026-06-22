import datetime

def get_day_of_week(date_string):
    try:
        parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
        return parsed_date.strftime("%A")
    except ValueError as e:
        raise ValueError(f"Invalid date format: {date_string}. Expected YYYY-MM-DD.") from e

if __name__ == '__main__':
    target_date = "2023-10-05"
    day_name = get_day_of_week(target_date)
    print(day_name)