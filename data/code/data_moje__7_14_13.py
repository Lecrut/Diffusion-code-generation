def convert_duration(total_seconds):
    if total_seconds < 0:
        raise ValueError("total_seconds must be non-negative")
    days = total_seconds // 86400
    remaining = total_seconds % 86400
    hours = remaining // 3600
    remaining %= 3600
    minutes = remaining // 60
    seconds = remaining % 60
    return days, hours, minutes, seconds

if __name__ == '__main__':
    test_values = [0, 59, 60, 3600, 86400, 90061, 172800, 8640000]
    for value in test_values:
        result = convert_duration(value)
        print(result)