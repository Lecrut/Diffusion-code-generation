from datetime import datetime
import pytz

def convert_pst_to_est(pst_time_str):
    pst = pytz.timezone('America/Los_Angeles')
    est = pytz.timezone('America/New_York')
    pst_time = datetime.strptime(pst_time_str, '%Y-%m-%d %H:%M:%S')
    pst_time = pst.localize(pst_time)
    est_time = pst_time.astimezone(est)
    time_difference = (est_time - pst_time).total_seconds() / 3600
    return (est_time, time_difference)
if __name__ == '__main__':
    sample_pst_time = '2023-10-05 14:00:00'
    est_time, time_difference = convert_pst_to_est(sample_pst_time)
    print(f"EST Time: {est_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f'Time Difference (hours): {time_difference}')