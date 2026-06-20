import datetime

def parse_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

def calculate_week_difference(date_str1, date_str2):
    date1 = parse_date(date_str1)
    date2 = parse_date(date_str2)
    time_difference = abs(date2 - date1)
    weeks = time_difference.days / 7.0
    return weeks

if __name__ == '__main__':
    date1 = "2023-01-01"
    date2 = "2023-01-08"
    result = calculate_week_difference(date1, date2)
    print(result)