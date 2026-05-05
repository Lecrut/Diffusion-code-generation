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
    date2_str = "2023-10-28 14:30:00"
    invalid_date_str = "26/10/2023 10:00"
    valid_date_str_2 = "2023-10-25 08:00:00"
    print(f"Calculating difference between: {date1_str} and {date2_str}")
    result1 = calculate_time_difference(date1_str, date2_str)
    print(f"Result 1: {result1}\n")
    print(f"Calculating difference between: {valid_date_str_2} and {date1_str}")
    result2 = calculate_time_difference(valid_date_str_2, date1_str)
    print(f"Result 2: {result2}\n")
    print(f"Testing with invalid format: {invalid_date_str} and {date2_str}")
    result3 = calculate_time_difference(invalid_date_str, date2_str)
    print(f"Result 3: {result3}\n")
    print(f"Testing with mixed invalid format: {date1_str} and {invalid_date_str}")
    result4 = calculate_time_difference(date1_str, invalid_date_str)
    print(f"Result 4: {result4}\n")