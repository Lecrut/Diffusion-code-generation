import datetime
import pytz
def convert_and_calculate_difference(pst_time_str):
    pst_tz = pytz.timezone('America/Los_Angeles')
    est_tz = pytz.timezone('America/New_York')
    pst_time = datetime.datetime.strptime(pst_time_str, '%Y-%m-%d %H:%M:%S')
    pst_tz_aware = pst_tz.localize(pst_time)
    est_tz_aware = est_tz.localize(pst_time)
    est_time = est_tz_aware.astimezone(est_tz)
    time_difference = est_time - pst_tz_aware
    return pst_time, est_time, time_difference
if __name__ == '__main__':
    sample_time = "2023-10-27 10:00:00"
    pst_time, est_time, diff = convert_and_calculate_difference(sample_time)
    print(f"PST Time: {pst_time}")
    print(f"EST Time: {est_time}")
    print(f"Time Difference (EST - PST): {diff}")