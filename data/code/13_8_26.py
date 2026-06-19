from datetime import datetime, timedelta

def convert_pst_to_est(pst_time):
    est_time = pst_time + timedelta(hours=7)
    return est_time
if __name__ == '__main__':
    sample_pst_time = datetime(2023, 10, 5, 9, 0)
    converted_est_time = convert_pst_to_est(sample_pst_time)
    print('PST Time:', sample_pst_time.strftime('%Y-%m-%d %H:%M:%S'))
    print('EST Time:', converted_est_time.strftime('%Y-%m-%d %H:%M:%S'))