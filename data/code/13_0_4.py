import datetime
import pytz
def calculate_time_difference(dt1_str, dt2_str):
    try:
        tz1 = pytz.timezone("America/New_York")
        tz2 = pytz.timezone("Europe/London")
        dt1 = pytz.timezone("UTC").localize(datetime.datetime.strptime(dt1_str, "%Y-%m-%d %H:%M:%S"))
        dt2 = pytz.timezone("UTC").localize(datetime.datetime.strptime(dt2_str, "%Y-%m-%d %H:%M:%S"))
        diff = dt2 - dt1
        return diff
    except Exception as e:
        return f"Error: {e}"
if __name__ == '__main__':
    time_string_1 = "2023-10-27 10:00:00"
    time_string_2 = "2023-10-27 14:30:00"
    time_difference = calculate_time_difference(time_string_1, time_string_2)
    print(time_difference)