import datetime

def get_weekday(date_string: str) -> str:
    parts = date_string.split("-")
    if len(parts) != 3:
        raise ValueError("Date string must be YYYY-MM-DD")
    year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
    date_obj = datetime.date(year, month, day)
    return date_obj.strftime("%A")

if __name__ == '__main__':
    target_date = "2023-12-25"
    weekday_name = get_weekday(target_date)
    print(weekday_name)