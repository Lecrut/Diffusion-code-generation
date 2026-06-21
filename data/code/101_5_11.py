import time

def get_weekday(date_str):
    try:
        struct_time = time.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}")
    
    timestamp = time.mktime(struct_time)
    weekday_index = time.localtime(timestamp).tm_wday
    
    weekdays = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    )
    
    if 0 <= weekday_index < 7:
        return weekdays[weekday_index]
    
    raise ValueError("Unexpected weekday index")

if __name__ == '__main__':
    sample_date = '2023-01-01'
    weekday_name = get_weekday(sample_date)
    print(weekday_name)