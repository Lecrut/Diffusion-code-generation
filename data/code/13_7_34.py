from datetime import datetime, timedelta

def convert_pst_to_est(pst_time_str):
    pst_time = datetime.strptime(pst_time_str, '%Y-%m-%d %H:%M:%S')
    time_difference = timedelta(hours=3)
    est_time = pst_time + time_difference
    return est_time
if __name__ == '__main__':
    pst_time_str = '2023-10-01 14:00:00'
    est_time = convert_pst_to_est(pst_time_str)
    print(est_time.strftime('%Y-%m-%d %H:%M:%S'))