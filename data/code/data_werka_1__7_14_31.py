def convert_seconds_to_dhms(total_seconds):
    days = total_seconds // (24 * 3600)
    hours = (total_seconds % (24 * 3600)) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return days, hours, minutes, seconds

if __name__ == '__main__':
    sample_values = [86400, 3600, 7200, 1800, 900, 60, 30, 15, 5, 1]
    for value in sample_values:
        print(convert_seconds_to_dhms(value))