import datetime
def calculate_week_difference(date_str1, date_str2):
    try:
        date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
        if date1 > date2:
            difference = abs(date1 - date2)
        else:
            difference = abs(date2 - date1)
        weeks = difference.days / 7.0
        print(f"The difference between {date_str1} and {date_str2} is approximately {weeks:.2f} weeks.")
    except ValueError:
        print("Error: Invalid date format. Please use YYYY-MM-DD.")
if __name__ == '__main__':
    date1_str = "2023-01-15"
    date2_str = "2023-02-28"
    calculate_week_difference(date1_str, date2_str)
    date1_str_invalid = "01/15/2023"
    date2_str_valid = "2023-02-28"
    calculate_week_difference(date1_str_invalid, date2_str_valid)