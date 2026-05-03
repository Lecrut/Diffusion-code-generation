import datetime
def convert_duration(time_str):
    h, m, s = map(int, time_str.split(':'))
    total_seconds = h * 3600 + m * 60 + s
    days = total_seconds // (24 * 3600)
    remaining_seconds = total_seconds % (24 * 3600)
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return f"{days} Days, {hours} Hours, {minutes} Minutes, {seconds} Seconds"
if __name__ == '__main__':
    sample_time1 = "25:60:00"
    sample_time2 = "10:30:15"
    sample_time3 = "0:0:5"
    print(convert_duration(sample_time1))
    print(convert_duration(sample_time2))
    print(convert_duration(sample_time3))