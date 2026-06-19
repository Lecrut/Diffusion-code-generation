from datetime import datetime
import pytz

def convert_pst_to_est(pst_time_str):
    pst = pytz.timezone('America/Los_Angeles')
    est = pytz.timezone('America/New_York')
    pst_time = pst.localize(datetime.strptime(pst_time_str, '%Y-%m-%d %H:%M:%S'))
    est_time = pst_time.astimezone(est)
    return est_time

def calculate_time_difference(pst_time_str):
    pst = pytz.timezone('America/Los_Angeles')
    est = pytz.timezone('America/New_York')
    pst_time = pst.localize(datetime.strptime(pst_time_str, '%Y-%m-%d %H:%M:%S'))
    est_time = pst_time.astimezone(est)
    time_difference = est_time - pst_time
    return time_difference
if __name__ == '__main__':
    sample_pst_time_str = '2023-10-05 14:00:00'
    est_time = convert_pst_to_est(sample_pst_time_str)
    time_difference = calculate_time_difference(sample_pst_time_str)
    print('PST Time:', sample_pst_time_str)
    print('Converted EST Time:', est_time.strftime('%Y-%m-%d %H:%M:%S'))
    print('Time Difference (EST - PST):', time_difference)