import datetime

def parse_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        try:
            return datetime.datetime.strptime(date_str, '%m/%d/%Y')
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD or MM/DD/YYYY.")

def calculate_days_difference(date1_str, date2_str):
    date1 = parse_date(date1_str)
    date2 = parse_date(date2_str)
    
    if date1 == date2:
        return 0
    elif date1 < date2:
        return (date2 - date1).days
    else:
        return (date1 - date2).days

if __name__ == '__main__':
    result = calculate_days_difference("2023-01-15", "2024-03-20")
    print(result)