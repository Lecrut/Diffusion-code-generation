from datetime import datetime

DATE_FORMAT = '%Y-%m-%d'

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, DATE_FORMAT)
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}. Must be 'YYYY-MM-DD'.")

def compare_dates(date_str1, date_str2):
    date1 = parse_date(date_str1)
    date2 = parse_date(date_str2)
    return min(date1, date2)

if __name__ == '__main__':
    date_a = "2023-10-26"
    date_b = "2023-10-25"
    earlier_date = compare_dates(date_a, date_b)
    print(f"Comparing {date_a} and {date_b}: {earlier_date}")