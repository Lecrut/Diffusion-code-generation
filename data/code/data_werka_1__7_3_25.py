def convert_time(duration_str):
    hours, minutes, seconds = map(int, duration_str.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    days = total_seconds // (24 * 3600)
    hours = (total_seconds % (24 * 3600)) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{days} Days, {hours} Hours, {minutes} Minutes, {seconds} Seconds"

if __name__ == '__main__':
    sample_duration = "48:30:15"
    print(convert_time(sample_duration))