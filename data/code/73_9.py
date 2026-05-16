import datetime
def calculate_time_difference(date_str1, date_str2):
    try:
        date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
        difference = date2 - date1
        return difference
    except ValueError:
        return "Error: Invalid date format. Please use YYYY-MM-DD."
if __name__ == '__main__':
    date1_str = "2023-01-15"
    date2_str = "2023-02-20"
    result = calculate_time_difference(date1_str, date2_str)
    print(f"Date 1: {date1_str}")
    print(f"Date 2: {date2_str}")
    print(f"Time Difference: {result}")
    invalid_date1_str = "15/01/2023"
    invalid_date2_str = "2023-02-20"
    result_error = calculate_time_difference(invalid_date1_str, invalid_date2_str)
    print(f"\nDate 1 (Invalid): {invalid_date1_str}")
    print(f"Date 2: {invalid_date2_str}")
    print(f"Time Difference (Error Handling): {result_error}")
    invalid_date1_str_2 = "2023-01-15T10:00:00"
    invalid_date2_str_2 = "2023-02-20"
    result_error_2 = calculate_time_difference(invalid_date1_str_2, invalid_date2_str_2)
    print(f"\nDate 1 (Invalid Format): {invalid_date1_str_2}")
    print(f"Date 2: {invalid_date2_str_2}")
    print(f"Time Difference (Error Handling): {result_error_2}")