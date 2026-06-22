import datetime

WEEKDAY_MAP = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def is_weekday(date_string: str) -> bool:
    if not isinstance(date_string, str):
        raise ValueError("Input must be a string")
    
    parts = date_string.split("-")
    if len(parts) != 3:
        raise ValueError("Invalid date format: expected YYYY-MM-DD")
    
    try:
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
    except ValueError:
        raise ValueError("Invalid date format: non-numeric components")
    
    if len(parts[0]) != 4 or len(parts[1]) != 2 or len(parts[2]) != 2:
        raise ValueError("Invalid date format: incorrect component lengths")
        
    try:
        date_obj = datetime.date(year, month, day)
        weekday_index = date_obj.weekday()
        return weekday_index < 5
    except ValueError:
        raise ValueError(f"Invalid date: {date_string}")

if __name__ == '__main__':
    test_cases = [
        "2023-10-07",
        "2023-10-08",
        "2023-02-28",
        "2023-02-29",
        "2023-13-01",
        "2023-01-00",
        "not-a-date",
        "2023-1-5"
    ]
    
    for date_str in test_cases:
        try:
            result = is_weekday(date_str)
            print(f"{date_str}: {result}")
        except ValueError as e:
            print(f"{date_str}: Error - {e}")