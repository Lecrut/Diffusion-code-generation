import datetime
def calculate_date_difference(date_string1, date_string2):
    date1 = None
    date2 = None
    formats = [
        "%Y-%m-%d",
        "%m/%d/%Y",
        "%d-%m-%Y",
        "%Y/%m/%d"
    ]
    for fmt in formats:
        try:
            date1 = datetime.datetime.strptime(date_string1, fmt)
        except ValueError:
            continue
    for fmt in formats:
        try:
            date2 = datetime.datetime.strptime(date_string2, fmt)
        except ValueError:
            continue
    if date1 is None or date2 is None:
        raise ValueError("Could not parse one or both date strings with known formats.")
    difference = abs(date1 - date2)
    return difference.days
if __name__ == '__main__':
    date_a = "2023-01-15"
    date_b = "02/20/2023"
    try:
        diff = calculate_date_difference(date_a, date_b)
        print(diff)
    except ValueError as e:
        print(f"Error: {e}")