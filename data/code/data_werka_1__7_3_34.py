def convert_time_duration(duration_str):
    hours, minutes, seconds = map(int, duration_str.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    days = total_seconds // (24 * 3600)
    total_seconds %= (24 * 3600)
    hours = total_seconds // 3600
    total_seconds %= 3600
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{days} Days, {hours} Hours, {minutes} Minutes, {seconds} Seconds"

if __name__ == '__main__':
    sample_duration = "48:35:21"
    human_readable_format = convert_time_duration(sample_duration)
    print(human_readable_format)