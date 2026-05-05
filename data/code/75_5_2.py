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
        except ValueError:
            continue
    for fmt in formats:
        try:
            if '/' in date_str2:
                date2 = datetime.datetime.strptime(date_str2, fmt)
            elif '-' in date_str2:
                date2 = datetime.datetime.strptime(date_str2, fmt)
            elif ':' in date_str2:
                date2 = datetime.datetime.strptime(date_str2, fmt)
            else:
                continue
        except ValueError:
            continue
    if date1 is None or date2 is None:
        return None
    return abs((date1 - date2).days)
if __name__ == '__main__':
    date_a = "12/31/2023"
    date_b = "2024-01-01"
    formats_to_try = ['%m/%d/%Y', '%Y-%m-%d']
    difference = calculate_date_difference(date_a, date_b, formats_to_try)
    print(difference)