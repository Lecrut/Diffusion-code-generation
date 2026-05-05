import datetime
def calculate_time_difference(date_str1, date_str2):
    try:
        date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
        difference = abs(date1 - date2)
        return difference.days
    except ValueError:
        return "Error: Invalid date format. Please use YYYY-MM-DD."
    except TypeError:
        return "Error: One or both inputs are not valid date strings."
if __name__ == '__main__':
    date1_str = "2023-01-15"
    date2_str = "2023-01-01"
    print(f"Comparing {date1_str} and {date2_str}: {calculate_time_difference(date1_str, date2_str)} days")
    date3_str = "2024-05-20"
    date4_str = "2024-05-10"
    print(f"Comparing {date3_str} and {date4_str}: {calculate_time_difference(date3_str, date4_str)} days")
    invalid_date_str = "2023/01/15"
    date5_str = "2023-01-01"
    print(f"Comparing {invalid_date_str} and {date5_str}: {calculate_time_difference(invalid_date_str, date5_str)}")
    date6_str = "2023-12-31"
    date7_str = "2023-12-31"
    print(f"Comparing {date6_str} and {date7_str}: {calculate_time_difference(date6_str, date7_str)} days")