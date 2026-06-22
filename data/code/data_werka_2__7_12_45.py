def convert_seconds_to_dhms(seconds):
    SECONDS_IN_DAY = 3600 * 24
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_MINUTE = 60

    days = seconds // SECONDS_IN_DAY
    remaining_seconds = seconds % SECONDS_IN_DAY

    hours = remaining_seconds // SECONDS_IN_HOUR
    remaining_seconds %= SECONDS_IN_HOUR

    minutes = remaining_seconds // SECONDS_IN_MINUTE
    remaining_seconds %= SECONDS_IN_MINUTE

    return days, hours, minutes, remaining_seconds

if __name__ == '__main__':
    sample_values = [1000000, 86400, 3661, 7200, 3600, 60, 0]
    for value in sample_values:
        print(convert_seconds_to_dhms(value))