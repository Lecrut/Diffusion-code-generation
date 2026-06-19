def convert_seconds_to_dhms(seconds):
    days = seconds // (24 * 3600)
    hours = (seconds % (24 * 3600)) // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return days, hours, minutes, remaining_seconds

if __name__ == '__main__':
    sample_values = [0, 86400, 3601, 7200, 90000]
    for value in sample_values:
        print(convert_seconds_to_dhms(value))