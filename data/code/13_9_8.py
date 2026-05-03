def convert_time_and_difference(pst_time_str):
    pst_time = pst_time_str.split(':')[0]
    pst_minutes = int(pst_time_str.split(':')[1])
    pst_hour = int(pst_time)
    pst_minute = pst_minutes
    est_hour = pst_hour + 3
    if est_hour >= 24:
        est_hour -= 24
    est_time = f"{est_hour}:{pst_minute}"
    time_difference_hours = 3
    return est_time, time_difference_hours
if __name__ == '__main__':
    sample_pst_time = "10:30"
    est_time, difference = convert_time_and_difference(sample_pst_time)
    print(f"PST Time: {sample_pst_time}")
    print(f"EST Time: {est_time}")
    print(f"Time Difference (EST - PST): {difference} hours")