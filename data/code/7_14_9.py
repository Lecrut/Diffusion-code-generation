def seconds_to_dhms(total_seconds):
    days = total_seconds // 86400
    remaining = total_seconds % 86400
    hours = remaining // 3600
    remaining %= 3600
    minutes = remaining // 60
    seconds = remaining % 60
    return days, hours, minutes, seconds

if __name__ == '__main__':
    sample_values = [0, 60, 3600, 86400, 90061, 172800, 2419200]
    for value in sample_values:
        result = seconds_to_dhms(value)
        print(f"{value} seconds -> {result}")