import datetime

WEEKDAY_NAMES = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def check_weekday_status(date_input):
    if isinstance(date_input, str):
        try:
            parsed_date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date string format: {date_input}")
    elif isinstance(date_input, datetime.date):
        parsed_date = date_input
    else:
        raise ValueError(f"Unsupported type: {type(date_input)}")
    
    day_index = parsed_date.weekday()
    day_name = WEEKDAY_NAMES.get(day_index, "Unknown")
    is_week = day_index < 5
    
    return {
        "date": parsed_date,
        "day_name": day_name,
        "is_weekday": is_week,
        "day_index": day_index
    }

if __name__ == '__main__':
    sample_date_str = "2023-10-07"
    result = check_weekday_status(sample_date_str)
    print(result)