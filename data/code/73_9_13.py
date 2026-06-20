from datetime import datetime

def calculate_time_difference(dt1, dt2):
    return abs(dt1 - dt2)

if __name__ == '__main__':
    sample_dt1 = datetime(2023, 10, 1, 12, 0, 0)
    sample_dt2 = datetime(2023, 10, 1, 14, 30, 0)
    print(calculate_time_difference(sample_dt1, sample_dt2))