def convert_time_and_calculate_difference(pst_time_str):
    pst_hour = int(pst_time_str.split(':')[0])
    pst_minute = int(pst_time_str.split(':')[1])
    time_difference_hours = 3
    est_hour = pst_hour + time_difference_hours
    est_minute = pst_minute
    return est_hour, est_minute, time_difference_hours
if __name__ == '__main__':
    sample_pst_time = "10:30"
    est_hour, est_minute, diff = convert_time_and_calculate_difference(sample_pst_time)
    print(f"PST Time: {sample_pst_time}")
    print(f"EST Time: {est_hour}:{est_minute}")
    print(f"Time Difference (EST ahead of PST): {diff} hours")