def convert_seconds_to_dhms(total_seconds):
    SECONDS_IN_DAY = 3600 * 24
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_MINUTE = 60

    days = total_seconds // SECONDS_IN_DAY
    remaining_seconds_after_days = total_seconds % SECONDS_IN_DAY

    hours = remaining_seconds_after_days // SECONDS_IN_HOUR
    remaining_seconds_after_hours = remaining_seconds_after_days % SECONDS_IN_HOUR

    minutes = remaining_seconds_after_hours // SECONDS_IN_MINUTE
    seconds = remaining_seconds_after_hours % SECONDS_IN_MINUTE

    return days, hours, minutes, seconds

if __name__ == '__main__':
    sample_duration = 1234567
    days, hours, minutes, seconds = convert_seconds_to_dhms(sample_duration)
    print(f"{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds")