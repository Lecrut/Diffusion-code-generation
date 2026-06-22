def convert_seconds_to_dhms(total_seconds):
    days = total_seconds // (24 * 3600)
    hours = (total_seconds % (24 * 3600)) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return days, hours, minutes, seconds

if __name__ == '__main__':
    sample_values = [0, 86400, 123456, 987654, 3600]
    for value in sample_values:
        print(convert_seconds_to_dhms(value))