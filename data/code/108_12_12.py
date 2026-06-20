from datetime import datetime

def parse_date_and_extract_day(date_string: str) -> int:
    if not isinstance(date_string, str):
        raise ValueError("Input must be a string.")
    
    date_format = "%Y-%m-%d"
    try:
        date_object = datetime.strptime(date_string, date_format)
        return date_object.day
    except ValueError as e:
        raise ValueError(f"Invalid date format. Please use {date_format}. Error: {e}")

if __name__ == '__main__':
    date_str = "2024-07-04"
    day_of_month = parse_date_and_extract_day(date_str)
    print(day_of_month)