import datetime

DATE_FORMAT = "%Y-%m-%d"
MONDAY = 0
SUNDAY = 6

def find_weekday_dates(date_strings):
    if not isinstance(date_strings, list):
        raise ValueError("Input must be a list of strings")
    
    result = []
    for date_str in date_strings:
        if not isinstance(date_str, str):
            raise ValueError("Each item must be a string")
        try:
            parsed_date = datetime.datetime.strptime(date_str, DATE_FORMAT)
            weekday = parsed_date.weekday()
            if MONDAY <= weekday <= SUNDAY:
                result.append(date_str)
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}")
    
    return result

if __name__ == '__main__':
    sample_dates = ["2023-10-01", "2023-10-02", "2023-10-07", "2023-10-08"]
    output = find_weekday_dates(sample_dates)
    print(output)