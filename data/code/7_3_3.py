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
    duration1 = "25:30:00"
    duration2 = "01:00:00"
    duration3 = "86:45:15"
    print(convert_duration(duration1))
    print(convert_duration(duration2))
    print(convert_duration(duration3))