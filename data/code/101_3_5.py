import datetime

def get_weekday(date_str):
    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        return date_obj.strftime("%A")
    except ValueError as e:
        raise ValueError(f"Invalid date format: {date_str}") from e

if __name__ == '__main__':
    sample_date = "2023-12-25"
    weekday_name = get_weekday(sample_date)
    print(weekday_name)