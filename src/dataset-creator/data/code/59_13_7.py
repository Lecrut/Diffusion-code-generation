import datetime
def get_weekday(day_string: str) -> int:
    try:
        date_obj = datetime.datetime.strptime(day_string, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Invalid date format '{day_string}'. Expected YYYY-MM-DD.")
    return date_obj.weekday()
if __name__ == '__main__':
    test_cases = [
        "2023-10-05",                  
        "2024-08-10",                 
        "2025-06-17",                
    ]
    for date_str in test_cases:
        print(f"{date_str} => {get_weekday(date_str)}")