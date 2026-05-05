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
    date1 = "2023-10-26"
    date2 = "2023-10-25"
    date3 = "2024-01-01"
    date4 = "2023-12-31"
    date5 = "2023-10-26"
    print(f"Comparing {date1} and {date2}: {compare_dates(date1, date2)}")
    print(f"Comparing {date2} and {date1}: {compare_dates(date2, date1)}")
    print(f"Comparing {date3} and {date4}: {compare_dates(date3, date4)}")
    print(f"Comparing {date4} and {date3}: {compare_dates(date4, date3)}")
    print(f"Comparing {date5} and {date5}: {compare_dates(date5, date5)}")
    print(f"Comparing {date1} and {date5}: {compare_dates(date1, date5)}")
    try:
        compare_dates("2023/10/26", "2023-10-25")
    except ValueError as e:
        print(f"Error caught: {e}")