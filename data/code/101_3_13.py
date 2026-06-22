import datetime

def get_weekday(date_string: str) -> str:
    try:
        date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
        return date_obj.strftime("%A")
    except ValueError:
        raise ValueError(f"Invalid date format: {date_string}")

if __name__ == '__main__':
    target_date = "2023-12-25"
    weekday_name = get_weekday(target_date)
    print(weekday_name)