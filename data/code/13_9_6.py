def convert_time(pst_time_str):
    pst_hour = int(pst_time_str.split(':')[0])
    pst_minute = int(pst_time_str.split(':')[1])
    est_hour = pst_hour + 3
    est_minute = pst_minute
    return f"{est_hour:02d}:{est_minute:02d}"
if __name__ == '__main__':
    sample_pst_time = "10:30"
    print(f"PST Time: {sample_pst_time}")
    est_time = convert_time(sample_pst_time)
    print(f"EST Time: {est_time}")
    time_difference = 3
    print(f"Time Difference (EST - PST): {time_difference} hours")