def convert_time(duration_str):
    hours, minutes, seconds = map(int, duration_str.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    days = total_seconds // (24 * 3600)
    remaining_seconds = total_seconds % (24 * 3600)
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return f"{days} Days, {hours} Hours, {minutes} Minutes, {seconds} Seconds"

if __name__ == '__main__':
    sample_duration = "48:30:15"
    print(convert_time(sample_duration))