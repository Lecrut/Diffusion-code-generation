import datetime

def parse_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError as e:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD HH:MM:SS'.")

def date_difference(date1, date2):
    if not isinstance(date1, datetime.datetime) or not isinstance(date2, datetime.datetime):
        raise TypeError("Both inputs must be datetime objects.")
    
    return abs((date2 - date1).total_seconds() / 60)

if __name__ == '__main__':
    try:
        date_a_str = "2023-10-29 10:00:00"
        date_b_str = "2023-11-02 14:30:00"
        
        date_a = parse_date(date_a_str)
        date_b = parse_date(date_b_str)
        
        difference = date_difference(date_a, date_b)
        print(f"Date difference in minutes: {difference}")
    except (ValueError, TypeError) as e:
        print(e)