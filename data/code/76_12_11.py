from datetime import datetime

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

def calculate_date_difference(date_str1, date_str2):
    date1 = parse_date(date_str1)
    date2 = parse_date(date_str2)
    return abs((date2 - date1).days)

if __name__ == '__main__':
    date1_str = "2023-01-15"
    date2_str = "2023-02-28"
    difference = calculate_date_difference(date1_str, date2_str)
    print(f"Date 1: {date1_str}")
    print(f"Date 2: {date2_str}")
    print(f"The difference between the two dates is {difference} days.")