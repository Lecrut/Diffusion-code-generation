from datetime import datetime
def calculate_time_difference(date_string1, date_string2):
    time1 = None
    time2 = None
    try:
        time1 = datetime.strptime(date_string1, '%Y-%m-%d %H:%M:%S')
        time2 = datetime.strptime(date_string2, '%Y-%m-%d %H:%M:%S')
        difference = time2 - time1
        return difference
    except ValueError:
        return "Error: Invalid date format. Please use YYYY-MM-DD HH:MM:SS"
    except TypeError:
        return "Error: One or both inputs are not valid date strings."
if __name__ == '__main__':
    date1_str = "2023-10-26 10:00:00"
    date2_str = "2023-10-27 14:30:00"
    date3_str = "2023/10/28 09:00:00"
    date4_str = "2023-10-26 10:00:00"
    print(f"Calculating difference between '{date1_str}' and '{date2_str}':")
    result1 = calculate_time_difference(date1_str, date2_str)
    print(result1)
    print("-" * 30)
    print(f"Calculating difference between '{date1_str}' and '{date3_str}' (Invalid format test):")
    result2 = calculate_time_difference(date1_str, date3_str)
    print(result2)
    print("-" * 30)
    print(f"Calculating difference between '{date4_str}' and '{date1_str}':")
    result3 = calculate_time_difference(date4_str, date1_str)
    print(result3)
    print("-" * 30)