import datetime
def calculate_time_difference(start_date_str, end_date_str):
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
    time_difference = end_date - start_date
    return time_difference
if __name__ == '__main__':
    start_date_input = "2023-01-15"
    end_date_input = "2024-05-20"
    elapsed_time = calculate_time_difference(start_date_input, end_date_input)
    print(f"Start Date: {start_date_input}")
    print(f"End Date: {end_date_input}")
    print(f"Time Elapsed (timedelta object): {elapsed_time}")
    print(f"Total days elapsed: {elapsed_time.days}")