def convert_seconds_to_dhms(seconds):
    days = seconds // (24 * 3600)
    hours = (seconds % (24 * 3600)) // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return days, hours, minutes, remaining_seconds

if __name__ == '__main__':
    sample_values = [86400, 90061, 3661, 7200, 123]
    for value in sample_values:
        print(convert_seconds_to_dhms(value))