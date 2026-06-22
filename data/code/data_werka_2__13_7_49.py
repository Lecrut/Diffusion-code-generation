from datetime import datetime, timedelta

TIME_ZONE_OFFSETS = {
    'PST': -8,
    'EST': -5
}

def convert_pst_to_est(pst_time_str):
    pst_time = datetime.strptime(pst_time_str, '%Y-%m-%d %H:%M:%S')
    utc_time = pst_time + timedelta(hours=TIME_ZONE_OFFSETS['PST'])
    est_time = utc_time + timedelta(hours=TIME_ZONE_OFFSETS['EST'])
    return est_time

def time_difference(pst_time_str, est_time):
    pst_time = datetime.strptime(pst_time_str, '%Y-%m-%d %H:%M:%S')
    return est_time - pst_time

if __name__ == '__main__':
    pst_time_str = '2023-10-05 14:00:00'
    est_time = convert_pst_to_est(pst_time_str)
    print('EST Time:', est_time.strftime('%Y-%m-%d %H:%M:%S'))
    diff = time_difference(pst_time_str, est_time)
    print('Time Difference:', diff)