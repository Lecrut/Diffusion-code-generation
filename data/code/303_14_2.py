import datetime
def calculate_time_difference(start_date_str, end_date_str):
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
    time_difference = end_date - start_date
    return time_difference
if __name__ == '__main__':
    start_date_value = "2023-01-15"
    end_date_value = "2023-05-20"
    time_elapsed = calculate_time_difference(start_date_value, end_date_value)
    print(f"Start Date: {start_date_value}")
    print(f"End Date: {end_date_value}")
    print(f"Time Elapsed (timedelta): {time_elapsed}")
    print(f"Days Elapsed: {time_elapsed.days}")