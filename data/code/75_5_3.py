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
            elif len(date_str1.split('/')) == 3:
                date1 = datetime.datetime.strptime(date_str1, fmt)
            elif len(date_str1.split('-')) == 3:
                date1 = datetime.datetime.strptime(date_str1, fmt)
        except ValueError:
            continue
    for fmt in formats:
        try:
            if '/' in date_str2:
                date2 = datetime.datetime.strptime(date_str2, fmt)
            elif '-' in date_str2:
                date2 = datetime.datetime.strptime(date_str2, fmt)
            elif len(date_str2.split('/')) == 3:
                date2 = datetime.datetime.strptime(date_str2, fmt)
            elif len(date_str2.split('-')) == 3:
                date2 = datetime.datetime.strptime(date_str2, fmt)
        except ValueError:
            continue
    if date1 and date2:
        return abs((date1 - date2).days)
    else:
        return None
if __name__ == '__main__':
    date1_str = "12/31/2023"
    date2_str = "01/01/2024"
    date1_format = "%m/%d/%Y"
    date2_format = "%m/%d/%Y"
    diff1 = calculate_date_difference(date1_str, date2_str, [date1_format, date2_format])
    print(f"Difference between {date1_str} and {date2_str} (MM/DD/YYYY format): {diff1}")
    date3_str = "2024-03-15"
    date4_str = "2024-03-01"
    date3_format = "%Y-%m-%d"
    date4_format = "%Y-%m-%d"
    diff2 = calculate_date_difference(date3_str, date4_str, [date3_format, date4_format])
    print(f"Difference between {date3_str} and {date4_str} (YYYY-MM-DD format): {diff2}")
    date5_str = "05/10/2023"
    date6_str = "2023-11-10"
    date5_format = "%m/%d/%Y"
    date6_format = "%Y-%m-%d"
    diff3 = calculate_date_difference(date5_str, date6_str, [date5_format, date6_format])
    print(f"Difference between {date5_str} and {date6_str} (Mixed format): {diff3}")