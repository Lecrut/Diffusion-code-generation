import datetime
def calculate_time_difference(date_str1, date_str2):
    try:
        date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
        difference = abs(date1 - date2)
        return difference.days
    except ValueError:
        return "Error: Invalid date format. Please use YYYY-MM-DD."
if __name__ == '__main__':
    date1_str = "2023-01-15"
    date2_str = "2022-11-20"
    date3_str = "2023/01/15"
    date4_str = "2023-1-15"
    date5_str = "2023-15-01"
    print(f"Difference between {date1_str} and {date2_str}: {calculate_time_difference(date1_str, date2_str)} days")
    print(f"Difference between {date1_str} and {date3_str}: {calculate_time_difference(date1_str, date3_str)}")
    print(f"Difference between {date1_str} and {date4_str}: {calculate_time_difference(date1_str, date4_str)}")
    print(f"Difference between {date1_str} and {date5_str}: {calculate_time_difference(date1_str, date5_str)}")