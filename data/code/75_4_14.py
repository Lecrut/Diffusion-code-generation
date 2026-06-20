import datetime

def parse_date(date_str):
    date_formats = ['%Y-%m-%d', '%m/%d/%Y']
    for format in date_formats:
        try:
            return datetime.datetime.strptime(date_str, format)
        except ValueError:
            continue
    raise ValueError("Error: Invalid date format. Please use YYYY-MM-DD or MM/DD/YYYY.")

def calculate_days_difference(date1_str, date2_str):
    try:
        date1 = parse_date(date1_str)
        date2 = parse_date(date2_str)
        if date1 == date2:
            return 0
        difference = abs((date2 - date1).days)
        return difference
    except ValueError as e:
        raise ValueError(e)

if __name__ == '__main__':
    date1_str = "01/15/2023"
    date2_str = "03/20/2024"
    result = calculate_days_difference(date1_str, date2_str)
    print(result)