from datetime import datetime

def is_valid_time(time_str):
    try:
        datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False

def convert_pst_to_est(pst_time_str):
    if not is_valid_time(pst_time_str):
        raise ValueError("Invalid time format. Please use 'YYYY-MM-DD HH:MM:SS'.")
    pst_time = datetime.strptime(pst_time_str, '%Y-%m-%d %H:%M:%S')
    time_difference = 3
    est_time = pst_time + timedelta(hours=time_difference)
    return est_time

def time_difference(pst_time, est_time):
    return est_time - pst_time
if __name__ == '__main__':
    pst_time_str = '2023-10-05 14:00:00'
    try:
        est_time = convert_pst_to_est(pst_time_str)
        print('EST Time:', est_time.strftime('%Y-%m-%d %H:%M:%S'))
        pst_time = datetime.strptime(pst_time_str, '%Y-%m-%d %H:%M:%S')
        diff = time_difference(pst_time, est_time)
        print('Time Difference:', diff)
    except ValueError as e:
        print(e)