from datetime import datetime
def calculate_time_difference(date_str1, date_str2):
    time1 = None
    time2 = None
    try:
        time1 = datetime.strptime(date_str1, '%Y-%m-%d %H:%M:%S')
        time2 = datetime.strptime(date_str2, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return None, "Invalid date format provided."
    if time1 is None or time2 is None:
        return None, "One or both dates could not be parsed."
    time_difference = time2 - time1
    return time_difference, None
if __name__ == '__main__':
    date1_valid = "2023-10-26 10:00:00"
    date2_valid = "2023-10-27 14:30:00"
    date1_invalid_format = "26/10/2023 10:00"
    date2_invalid_format = "2023-10-27 14:30:00"
    date1_invalid_date = "2023-13-01 10:00:00"
    print("--- Test Case 1: Valid Dates ---")
    diff1, error1 = calculate_time_difference(date1_valid, date2_valid)
    if error1:
        print(f"Error: {error1}")
    else:
        print(f"Date 1: {date1_valid}")
        print(f"Date 2: {date2_valid}")
        print(f"Time Difference: {diff1}")
    print("\n--- Test Case 2: Invalid Format for First Date ---")
    diff2, error2 = calculate_time_difference(date1_invalid_format, date2_valid)
    if error2:
        print(f"Error: {error2}")
    else:
        print(f"Time Difference: {diff2}")
    print("\n--- Test Case 3: Invalid Date Value (Month out of range) ---")
    diff3, error3 = calculate_time_difference(date1_valid, date1_invalid_date)
    if error3:
        print(f"Error: {error3}")
    else:
        print(f"Time Difference: {diff3}")
    print("\n--- Test Case 4: Both Invalid Formats ---")
    diff4, error4 = calculate_time_difference(date1_invalid_format, date1_invalid_date)
    if error4:
        print(f"Error: {error4}")
    else:
        print(f"Time Difference: {diff4}")