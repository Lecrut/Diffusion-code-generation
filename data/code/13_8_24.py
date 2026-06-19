from datetime import datetime, timedelta

def convert_pst_to_est(pst_time):
    time_difference = timedelta(hours=3)
    est_time = pst_time + time_difference
    return est_time
if __name__ == '__main__':
    sample_pst_time = datetime(2023, 10, 1, 14, 0)
    est_time = convert_pst_to_est(sample_pst_time)
    print('PST Time:', sample_pst_time.strftime('%Y-%m-%d %I:%M %p'))
    print('EST Time:', est_time.strftime('%Y-%m-%d %I:%M %p'))