import datetime
def calculate_days_between(date_str1, date_str2):
    date1 = None
    date2 = None
    formats = [
        "%Y-%m-%d",
        "%m/%d/%Y",
        "%d-%m-%Y",
        "%Y/%m/%d",
        "%m-%d-%Y"
    ]
    for fmt in formats:
        try:
            date1 = datetime.datetime.strptime(date_str1, fmt).date()
            date2 = datetime.datetime.strptime(date_str2, fmt).date()
            return abs((date1 - date2).days)
        except ValueError:
            continue
    raise ValueError("Could not parse the dates with any known format.")
if __name__ == '__main__':
    date_a = "2023-01-15"
    date_b = "2023/01/20"
    try:
        days = calculate_days_between(date_a, date_b)
        print(days)
    except ValueError as e:
        print(f"Error: {e}")