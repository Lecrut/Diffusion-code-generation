def convert_seconds(total_seconds):
    if total_seconds >= 3600:
        hours = total_seconds // 3600
        remaining_seconds = total_seconds % 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        return f"{hours} hours, {minutes} minutes, {seconds} seconds"
    elif total_seconds >= 60:
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes} minutes, {seconds} seconds"
    else:
        return f"{total_seconds} seconds"

if __name__ == '__main__':
    test_values = [45, 120, 3665, 7200]
    for value in test_values:
        result = convert_seconds(value)
        print(f"{value} seconds -> {result}")