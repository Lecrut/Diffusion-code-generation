import sys
def compare_dates_lexicographically(date_str1, date_str2):
    if date_str1 < date_str2:
        return -1
    elif date_str1 > date_str2:
        return 1
    else:
        return 0
if __name__ == '__main__':
    date1 = "2023-10-26"
    date2 = "2023-10-27"
    date3 = "2024-01-01"
    date4 = "2023-12-31"
    date5 = "2023-10-26"
    print(f"Comparing {date1} and {date2}: {compare_dates_lexicographically(date1, date2)}")
    print(f"Comparing {date2} and {date1}: {compare_dates_lexicographically(date2, date1)}")
    print(f"Comparing {date3} and {date4}: {compare_dates_lexicographically(date3, date4)}")
    print(f"Comparing {date4} and {date3}: {compare_dates_lexicographically(date4, date3)}")
    print(f"Comparing {date1} and {date5}: {compare_dates_lexicographically(date1, date5)}")
    print(f"Comparing {date5} and {date1}: {compare_dates_lexicographically(date5, date1)}")