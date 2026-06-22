def convert_seconds(total_seconds):
    days = total_seconds // (24 * 3600)
    remaining_seconds = total_seconds % (24 * 3600)
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return days, hours, minutes, seconds

if __name__ == '__main__':
    sample_values = [86400, 7200, 180, 95, 0]
    for value in sample_values:
        print(convert_seconds(value))