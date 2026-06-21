def convert_seconds_to_dhms(total_seconds):
    days = total_seconds // (3600 * 24)
    hours = (total_seconds % (3600 * 24)) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return days, hours, minutes, seconds

if __name__ == '__main__':
    sample_values = [86400, 3661, 7200, 3600, 60, 59, 0]
    for value in sample_values:
        result = convert_seconds_to_dhms(value)
        print(result)