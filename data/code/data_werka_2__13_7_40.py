from datetime import datetime, timedelta

def convert_pst_to_est(pst_time_str):
    pst_to_est_offset = timedelta(hours=3)
    pst_time = datetime.strptime(pst_time_str, '%Y-%m-%d %H:%M:%S')
    est_time = pst_time + pst_to_est_offset
    return est_time
if __name__ == '__main__':
    sample_pst_time = '2023-10-05 14:00:00'
    converted_est_time = convert_pst_to_est(sample_pst_time)
    print(f'Original PST Time: {sample_pst_time}')
    print(f"Converted EST Time: {converted_est_time.strftime('%Y-%m-%d %H:%M:%S')}")