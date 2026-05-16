from datetime import datetime
def calculate_time_difference(date_string1, date_string2):
    time1 = None
    time2 = None
    try:
        time1 = datetime.strptime(date_string1, '%Y-%m-%d %H:%M:%S')
        time2 = datetime.strptime(date_string2, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return None, "Error: Invalid date format. Please use YYYY-MM-DD HH:MM:SS format."
    if time1 is None or time2 is None:
        return None, "Error: One or both dates could not be parsed."
    difference = time2 - time1
    return difference, None
if __name__ == '__main__':
    date1_valid = "2023-10-26 10:00:00"
    date2_valid = "2023-10-26 12:30:00"
    date1_invalid = "26/10/2023 10:00"
    date2_invalid = "2023-10-26 12:30:00"
    date3_invalid = "2023-10-26 10:00:00"
    date4_invalid = "NotADate"
    print("--- Test Case 1: Valid Dates ---")
    diff1, error1 = calculate_time_difference(date1_valid, date2_valid)
    if error1:
        print(f"Result: {error1}")
    else:
        print(f"Date 1: {date1_valid}")
        print(f"Date 2: {date2_valid}")
        print(f"Time Difference: {diff1}")
        print("-" * 20)
    print("--- Test Case 2: Invalid Format for First Date ---")
    diff2, error2 = calculate_time_difference(date1_invalid, date2_valid)
    if error2:
        print(f"Result: {error2}")
    else:
        print(f"Time Difference: {diff2}")
        print("-" * 20)
    print("--- Test Case 3: Invalid Format for Both Dates ---")
    diff3, error3 = calculate_time_difference(date1_invalid, date4_invalid)
    if error3:
        print(f"Result: {error3}")
    else:
        print(f"Time Difference: {diff3}")
        print("-" * 20)
    print("--- Test Case 4: Valid Dates with Different Order ---")
    diff4, error4 = calculate_time_difference(date2_valid, date1_valid)
    if error4:
        print(f"Result: {error4}")
    else:
        print(f"Date 1: {date2_valid}")
        print(f"Date 2: {date1_valid}")
        print(f"Time Difference: {diff4}")
        print("-" * 20)