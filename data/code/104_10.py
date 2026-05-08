import datetime
def calculate_days_between(date_str1, date_str2):
    date1 = None
    date2 = None
    formats = ["%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y", "%Y/%m/%d"]
    for fmt in formats:
        try:
            date1 = datetime.datetime.strptime(date_str1, fmt)
        except ValueError:
            continue
    for fmt in formats:
        try:
            date2 = datetime.datetime.strptime(date_str2, fmt)
        except ValueError:
            continue
    if date1 and date2:
        return abs((date2 - date1).days)
    else:
        raise ValueError("Could not parse one or both date strings with known formats.")
if __name__ == '__main__':
    date_a = "2023-01-15"
    date_b = "02/20/2023"
    try:
        days = calculate_days_between(date_a, date_b)
        print(days)
    except ValueError as e:
        print(f"Error: {e}")