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
            date1 = datetime.datetime.strptime(date_string1, fmt).date()
        except ValueError:
            continue
    for fmt in formats:
        try:
            date2 = datetime.datetime.strptime(date_string2, fmt).date()
        except ValueError:
            continue
    if date1 is None or date2 is None:
        raise ValueError("Could not parse one or both date strings with known formats.")
    difference = abs(date1 - date2).days
    return difference
if __name__ == '__main__':
    date_str1 = "2023-10-26"
    date_str2 = "11/15/2023"
    try:
        diff = calculate_date_difference(date_str1, date_str2)
        print(diff)
    except ValueError as e:
        print(f"Error: {e}")