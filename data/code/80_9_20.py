from datetime import datetime

def parse_date(date_string: str) -> datetime:
    date_formats = ["%Y-%m-%d", "%m/%d/%Y", "%d.%m.%Y"]
    for fmt in date_formats:
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            continue
    raise ValueError("Invalid date format")

def compare_dates(date1: datetime, date2: datetime) -> str:
    if date1 < date2:
        return "date1 is earlier than date2"
    elif date1 > date2:
        return "date1 is later than date2"
    else:
        return "date1 and date2 are the same"

if __name__ == '__main__':
    try:
        date_str1 = "05/15/2023"
        date_str2 = "2023.10.01"
        
        parsed_date1 = parse_date(date_str1)
        parsed_date2 = parse_date(date_str2)
        
        result = compare_dates(parsed_date1, parsed_date2)
        print(result)
    except ValueError as e:
        print(e)