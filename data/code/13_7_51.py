from datetime import datetime, timedelta

class TimeConverter:
    PST_OFFSET = -8
    EST_OFFSET = -5

    @staticmethod
    def convert_pst_to_est(pst_time_str):
        pst_time = datetime.strptime(pst_time_str, '%Y-%m-%d %H:%M:%S')
        utc_time = pst_time + timedelta(hours=TimeConverter.PST_OFFSET)
        est_time = utc_time + timedelta(hours=TimeConverter.EST_OFFSET)
        return est_time

    @staticmethod
    def time_difference(pst_time_str, est_time):
        pst_time = datetime.strptime(pst_time_str, '%Y-%m-%d %H:%M:%S')
        return est_time - pst_time

if __name__ == '__main__':
    pst_time_str = '2023-10-05 14:00:00'
    est_time = TimeConverter.convert_pst_to_est(pst_time_str)
    print('EST Time:', est_time.strftime('%Y-%m-%d %H:%M:%S'))
    diff = TimeConverter.time_difference(pst_time_str, est_time)
    print('Time Difference:', diff)