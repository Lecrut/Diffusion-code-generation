def convert_seconds_to_dhms(seconds):
    days = seconds // (3600 * 24)
    hours = (seconds % (3600 * 24)) // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return days, hours, minutes, remaining_seconds

if __name__ == '__main__':
    sample_values = [0, 86400, 123456, 90061, 3600]
    for value in sample_values:
        print(convert_seconds_to_dhms(value))