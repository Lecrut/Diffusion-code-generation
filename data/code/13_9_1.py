import datetime
import pytz
def convert_and_calculate_difference(pst_time_str):
    pst_tz = pytz.timezone('America/Los_Angeles')
    est_tz = pytz.timezone('America/New_York')
    pst_tz_obj = pst_tz.localize(datetime.datetime.strptime(pst_time_str, '%Y-%m-%d %H:%M:%S'))
    pst_datetime = pst_tz_obj.astimezone(pytz.utc)
    est_datetime = pst_tz_obj.astimezone(est_tz)
    time_difference = est_datetime - pst_datetime
    return pst_datetime, est_datetime, time_difference
if __name__ == '__main__':
    sample_pst_time = "2023-10-27 10:00:00"
    pst_utc, est_time, diff = convert_and_calculate_difference(sample_pst_time)
    print(f"PST Time (UTC equivalent): {pst_utc}")
    print(f"EST Time: {est_time}")
    print(f"Time Difference (EST - PST): {diff}")