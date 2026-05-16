from datetime import datetime
def calculate_date_difference(date_str1, date_str2, formats):
    date1 = None
    date2 = None
    for fmt in formats:
        try:
            if '/' in date_str1:
                date1 = datetime.strptime(date_str1, fmt)
            elif '-' in date_str1:
                date1 = datetime.strptime(date_str1, fmt)
            elif ':' in date_str1:
                date1 = datetime.strptime(date_str1, fmt)
            else:
                continue
        except ValueError:
            continue
    for fmt in formats:
        try:
            if '/' in date_str2:
                date2 = datetime.strptime(date_str2, fmt)
            elif '-' in date_str2:
                date2 = datetime.strptime(date_str2, fmt)
            elif ':' in date_str2:
                date2 = datetime.strptime(date_str2, fmt)
            else:
                continue
        except ValueError:
            continue
    if date1 and date2:
        return abs((date1 - date2).days)
    else:
        raise ValueError("Could not parse one or both dates with the provided formats.")
if __name__ == '__main__':
    date_a = "12/31/2023"
    date_b = "2024-01-05"
    date_c = "2023-12-31"
    date_d = "01/01/2024"
    formats_to_try = ['%m/%d/%Y', '%Y-%m-%d']
    try:
        diff1 = calculate_date_difference(date_a, date_b, formats_to_try)
        print(f"Difference between {date_a} and {date_b}: {diff1} days")
        diff2 = calculate_date_difference(date_c, date_d, formats_to_try)
        print(f"Difference between {date_c} and {date_d}: {diff2} days")
    except ValueError as e:
        print(f"Error: {e}")