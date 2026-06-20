import datetime

def parse_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError as e:
        raise ValueError("Invalid date format: must be 'YYYY-MM-DD HH:MM:SS'") from e

def date_difference(date1, date2):
    if not isinstance(date1, datetime.datetime) or not isinstance(date2, datetime.datetime):
        raise TypeError("Both arguments must be instances of datetime.datetime")
    
    return abs((date2 - date1).total_seconds() / 60)

if __name__ == '__main__':
    date_a_str = "2023-10-29 10:00:00"
    date_b_str = "2023-11-02 14:30:00"
    
    try:
        date_a = parse_date(date_a_str)
        date_b = parse_date(date_b_str)
        difference = date_difference(date_a, date_b)
        print(difference)
    except (ValueError, TypeError) as e:
        print(e)