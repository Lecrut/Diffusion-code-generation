import datetime
def calculate_date_difference(date_str1, date_str2):
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
            date1 = datetime.datetime.strptime(date_str1, fmt)
        except ValueError:
            continue
    for fmt in formats:
        try:
            date2 = datetime.datetime.strptime(date_str2, fmt)
        except ValueError:
            continue
    if date1 is None or date2 is None:
        raise ValueError("Could not parse one or both date strings with known formats.")
    return abs((date1 - date2).days)
if __name__ == '__main__':
    date1_input = "2023-10-26"
    date2_input = "11/15/2023"
    try:
        difference = calculate_date_difference(date1_input, date2_input)
        print(difference)
    except ValueError as e:
        print(f"Error: {e}")