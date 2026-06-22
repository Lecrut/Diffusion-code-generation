def convert_seconds(total_seconds):
    if total_seconds >= 3600:
        hours = total_seconds // 3600
        remaining = total_seconds % 3600
        return f"{hours} hours"
    if total_seconds >= 60:
        minutes = total_seconds // 60
        remaining = total_seconds % 60
        return f"{minutes} minutes"
    return f"{total_seconds} seconds"

if __name__ == '__main__':
    test_values = [45, 125, 3700, 86400, 60, 0]
    for value in test_values:
        result = convert_seconds(value)
        print(f"{value} seconds is {result}")