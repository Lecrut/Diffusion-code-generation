import datetime
import pytz
def convert_and_compare_time(pst_time_str):
    pst_tz = pytz.timezone('America/Los_Angeles')
    est_tz = pytz.timezone('America/New_York')
    pst_time_str = pst_time_str.strip()
    pst_time = datetime.datetime.strptime(pst_time_str, '%Y-%m-%d %H:%M:%S')
    pst_tz_aware = pst_tz.localize(pst_time)
    est_tz_aware = est_tz.localize(pst_time)
    est_time = est_tz_aware.astimezone(est_tz)
    time_difference = (est_time - pst_tz_aware).total_seconds()
    return pst_time_str, est_time.strftime('%Y-%m-%d %H:%M:%S'), time_difference
if __name__ == '__main__':
    sample_pst_time = "2023-10-27 10:00:00"
    pst_time_str, est_time_str, diff = convert_and_compare_time(sample_pst_time)
    print(f"PST Time: {pst_time_str}")
    print(f"EST Time: {est_time_str}")
    print(f"Time Difference (EST - PST): {diff / 3600:.2f} hours")