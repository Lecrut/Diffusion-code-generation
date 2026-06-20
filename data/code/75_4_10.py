import datetime

def parse_date(date_str):
    for fmt in ('%m/%d/%Y', '%Y-%m-%d'):
        try:
            return datetime.datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError("Error: Invalid date format. Please use MM/DD/YYYY or YYYY-MM-DD.")

def calculate_days_difference(date1_str, date2_str):
    date1 = parse_date(date1_str)
    date2 = parse_date(date2_str)
    return abs((date2 - date1).days)

if __name__ == '__main__':
    date1 = "07/31/2022"
    date2 = "2023-01-15"
    result = calculate_days_difference(date1, date2)
    print(result)