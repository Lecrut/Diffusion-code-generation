import datetime

def get_weekday_name(date_str):
    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        return date_obj.strftime("%A")
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}")

if __name__ == '__main__':
    target_date = "2023-10-05"
    day_name = get_weekday_name(target_date)
    print(day_name)