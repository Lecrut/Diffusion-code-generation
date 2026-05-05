import datetime
def are_dates_identical(date_str1, date_str2):
    date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d').date()
    date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d').date()
    return date1 == date2
if __name__ == '__main__':
    date1_str = "2023-10-27"
    date2_str = "2023-10-27"
    date3_str = "2023-10-28"
    print(f"Comparing {date1_str} and {date2_str}: {are_dates_identical(date1_str, date2_str)}")
    print(f"Comparing {date1_str} and {date3_str}: {are_dates_identical(date1_str, date3_str)}")