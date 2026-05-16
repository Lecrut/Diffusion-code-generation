def convert_time_and_calculate_difference(pst_time_str):
    pst_hour = int(pst_time_str.split(':')[0])
    pst_minute = int(pst_time_str.split(':')[1])
    est_hour = pst_hour + 3
    est_minute = pst_minute
    time_difference_hours = 3
    return f"PST Time: {pst_hour:02d}:{pst_minute:02d}\nEST Time: {est_hour:02d}:{est_minute:02d}\nTime Difference (EST - PST): {time_difference_hours} hours"
if __name__ == '__main__':
    sample_pst_time = "14:30"
    result = convert_time_and_calculate_difference(sample_pst_time)
    print(result)