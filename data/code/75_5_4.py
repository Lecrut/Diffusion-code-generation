import datetime
def calculate_date_difference(date_str1, date_str2, formats):
    date1 = None
    date2 = None
    for fmt in formats:
        try:
            if '/' in date_str1:
                date1 = datetime.datetime.strptime(date_str1, fmt)
            elif '-' in date_str1:
                date1 = datetime.datetime.strptime(date_str1, fmt)
            elif ':' in date_str1:
                date1 = datetime.datetime.strptime(date_str1, fmt)
            else:
                continue
            if '/' in date_str2:
                date2 = datetime.datetime.strptime(date_str2, fmt)
            elif '-' in date_str2:
                date2 = datetime.datetime.strptime(date_str2, fmt)
            elif ':' in date_str2:
                date2 = datetime.datetime.strptime(date_str2, fmt)
            else:
                continue
            if date1 and date2:
                return abs((date1 - date2).days)
        except ValueError:
            continue
    return None
if __name__ == '__main__':
    date_a = "10/25/2023"
    date_b = "2023-11-15"
    formats_to_try = [
        "%m/%d/%Y",
        "%Y-%m-%d"
    ]
    difference = calculate_date_difference(date_a, date_b, formats_to_try)
    print(difference)