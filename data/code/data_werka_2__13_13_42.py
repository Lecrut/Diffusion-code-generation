def convert_seconds_to_dhms(seconds):
    days = seconds // (3600 * 24)
    hours = (seconds % (3600 * 24)) // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return days, hours, minutes, remaining_seconds

if __name__ == '__main__':
    sample_duration = 987654
    days, hours, minutes, remaining_seconds = convert_seconds_to_dhms(sample_duration)
    print(f"{days} days, {hours} hours, {minutes} minutes, {remaining_seconds} seconds")