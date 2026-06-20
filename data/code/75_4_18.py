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
    if date1 < date2:
        difference = date2 - date1
    else:
        difference = date1 - date2
    return difference.days

if __name__ == '__main__':
    date1 = "2023-01-15"
    date2 = "03/20/2024"
    result = calculate_days_difference(date1, date2)
    print(result)