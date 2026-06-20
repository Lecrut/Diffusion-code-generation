import datetime

def parse_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD HH:MM:SS'.")

def calculate_difference(date1, date2):
    if date1 > date2:
        return (date1 - date2).total_seconds() / 60
    else:
        return (date2 - date1).total_seconds() / 60

if __name__ == '__main__':
    date_a_str = "2023-10-29 10:00:00"
    date_b_str = "2023-11-02 14:30:00"
    
    try:
        date_a = parse_date(date_a_str)
        date_b = parse_date(date_b_str)
        difference = calculate_difference(date_a, date_b)
        print(f"The difference in minutes is: {difference}")
    except ValueError as e:
        print(e)