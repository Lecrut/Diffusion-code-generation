from datetime import datetime, timedelta

def convert_pst_to_est(pst_time_str):
    pst_offset = -8
    est_offset = -5
    pst_time = datetime.strptime(pst_time_str, '%Y-%m-%d %H:%M:%S')
    utc_time = pst_time + timedelta(hours=pst_offset)
    est_time = utc_time + timedelta(hours=est_offset)
    return est_time

def time_difference(pst_time_str):
    est_time = convert_pst_to_est(pst_time_str)
    pst_time = datetime.strptime(pst_time_str, '%Y-%m-%d %H:%M:%S')
    time_diff = (est_time - pst_time).total_seconds() / 3600
    return time_diff
if __name__ == '__main__':
    pst_time_str = '2023-10-05 14:00:00'
    est_time = convert_pst_to_est(pst_time_str)
    print('EST Time:', est_time.strftime('%Y-%m-%d %H:%M:%S'))
    diff_hours = time_difference(pst_time_str)
    print('Time Difference (hours):', diff_hours)