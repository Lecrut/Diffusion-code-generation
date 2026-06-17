import datetime
def calculate_day_number(year, month, day):
    try:
        date = datetime.date(year, month, day)
        return date.timetuple().tm_yday
    except ValueError:
        return None
if __name__ == '__main__':
    test_year = 2023
    test_month = 10
    test_day = 27
    result = calculate_day_number(test_year, test_month, test_day)
    print(f"The day number for {test_year}-{test_month}-{test_day} is: {result}")
    test_invalid_month = 13
    result_invalid = calculate_day_number(2023, test_invalid_month, 1)
    print(f"The day number for an invalid month (13) is: {result_invalid}")