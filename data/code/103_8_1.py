import datetime
def calculate_time_difference(current_time_str):
    current_time = datetime.datetime.strptime(current_time_str, "%Y-%m-%d %H:%M:%S")
    start_of_day = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
    difference = current_time - start_of_day
    return difference
if __name__ == '__main__':
    sample_time = "2023-10-27 14:35:10"
    difference = calculate_time_difference(sample_time)
    print(f"Current Time: {sample_time}")
    print(f"Start of Day: {datetime.datetime.strptime(sample_time, '%Y-%m-%d %H:%M:%S').date()}")
    print(f"Difference (Time elapsed since start of day): {difference}")