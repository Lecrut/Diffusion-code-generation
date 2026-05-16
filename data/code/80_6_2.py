import sys
def compare_dates(date_str1, date_str2):
    parts1 = date_str1.split('-')
    parts2 = date_str2.split('-')
    if len(parts1) != 3 or len(parts2) != 3:
        raise ValueError("Date strings must be in 'YYYY-MM-DD' format.")
    try:
        year1 = int(parts1[0])
        month1 = int(parts1[1])
        day1 = int(parts1[2])
        year2 = int(parts2[0])
        month2 = int(parts2[1])
        day2 = int(parts2[2])
    except ValueError:
        raise ValueError("Date components must be valid integers.")
    if year1 != year2:
        return year1 - year2
    if month1 != month2:
        return month1 - month2
    if day1 != day2:
        return day1 - day2
    return 0
if __name__ == '__main__':
    date_a = "2023-10-26"
    date_b = "2023-10-25"
    date_c = "2024-01-01"
    date_d = "2023-10-26"
    date_e = "2023-10-27"
    print(f"Comparing {date_a} and {date_b}: {compare_dates(date_a, date_b)}")
    print(f"Comparing {date_a} and {date_c}: {compare_dates(date_a, date_c)}")
    print(f"Comparing {date_d} and {date_a}: {compare_dates(date_d, date_a)}")
    print(f"Comparing {date_e} and {date_a}: {compare_dates(date_e, date_a)}")
    print(f"Comparing {date_a} and {date_a}: {compare_dates(date_a, date_a)}")
    print(f"Comparing {date_b} and {date_e}: {compare_dates(date_b, date_e)}")
    try:
        compare_dates("2023/10/26", "2023-10-25")
    except ValueError as e:
        print(f"Error caught: {e}")