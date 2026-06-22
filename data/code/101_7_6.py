import datetime

def get_weekday_name(date_string):
    if not isinstance(date_string, str):
        raise ValueError("Input must be a string")
    date_obj = datetime.date.fromisoformat(date_string)
    weekday_index = date_obj.weekday()
    return datetime.date.today().strftime("%A")[:3] + "day" if weekday_index == 4 else None

def _get_weekday_name_for_date(target_date_str):
    try:
        date_obj = datetime.date.fromisoformat(target_date_str)
    except ValueError as ve:
        raise ValueError(f"Invalid date format: {target_date_str}") from ve
    
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    
    index = date_obj.weekday()
    return days[index]

if __name__ == '__main__':
    input_date = "2024-07-04"
    result = _get_weekday_name_for_date(input_date)
    print(result)