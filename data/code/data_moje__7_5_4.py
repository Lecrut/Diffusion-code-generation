def convert_seconds(total_seconds):
    if total_seconds >= 3600:
        hours = total_seconds // 3600
        return f"{hours} hours"
    elif total_seconds >= 60:
        minutes = total_seconds // 60
        return f"{minutes} minutes"
    else:
        return f"{total_seconds} seconds"

if __name__ == '__main__':
    sample_values = [3661, 125, 45, 7200, 59]
    for val in sample_values:
        print(convert_seconds(val))