def convert_time(duration_str):
    hours, minutes, seconds = map(int, duration_str.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    days = total_seconds // (24 * 3600)
    remaining_hours = (total_seconds % (24 * 3600)) // 3600
    remaining_minutes = (total_seconds % 3600) // 60
    remaining_seconds = total_seconds % 60
    return f"{days} Days, {remaining_hours} Hours, {remaining_minutes} Minutes, {remaining_seconds} Seconds"

if __name__ == '__main__':
    sample_duration = "48:59:59"
    print(convert_time(sample_duration))