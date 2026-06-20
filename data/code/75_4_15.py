import datetime

def parse_date(date_str):
    formats = ['%Y-%m-%d', '%m/%d/%Y']
    for fmt in formats:
        try:
            return datetime.datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError("Invalid date format. Please use YYYY-MM-DD or MM/DD/YYYY.")

def calculate_days_difference(date1_str, date2_str):
    try:
        date1 = parse_date(date1_str)
        date2 = parse_date(date2_str)
        difference = abs((date2 - date1).days)
        return difference
    except ValueError as e:
        return f"Error parsing date: {e}"

if __name__ == '__main__':
    date1 = "01/15/2023"
    date2 = "2024-03-20"
    result = calculate_days_difference(date1, date2)
    print(result)