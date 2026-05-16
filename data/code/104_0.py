import datetime
def compare_dates(date_str1, date_str2):
    try:
        date1 = datetime.datetime.strptime(date_str1, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(date_str2, "%Y-%m-%d")
        if date1 > date2:
            return f"{date_str1} is chronologically later than {date_str2}"
        elif date2 > date1:
            return f"{date_str2} is chronologically later than {date_str1}"
        else:
            return f"{date_str1} and {date_str2} are the same date"
    except ValueError:
        return "Error: One or both date strings are not in the expected YYYY-MM-DD format."
if __name__ == '__main__':
    date1_input = "2023-10-26"
    date2_input = "2023-11-15"
    result = compare_dates(date1_input, date2_input)
    print(result)
    date3_input = "2024-01-01"
    date4_input = "2024-01-01"
    result2 = compare_dates(date3_input, date4_input)
    print(result2)
    date5_input = "2025-05-05"
    date6_input = "2025-05-04"
    result3 = compare_dates(date5_input, date6_input)
    print(result3)
    date7_input = "2023/10/26"
    date8_input = "2023-10-26"
    result4 = compare_dates(date7_input, date8_input)
    print(result4)