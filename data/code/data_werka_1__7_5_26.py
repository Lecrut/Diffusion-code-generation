def convert_seconds(total_seconds):
    if total_seconds >= 3600:
        return f"{total_seconds // 3600} hours"
    elif total_seconds >= 60:
        return f"{total_seconds // 60} minutes"
    else:
        return f"{total_seconds} seconds"

if __name__ == '__main__':
    sample_values = [45, 90, 1800, 3601]
    for value in sample_values:
        print(convert_seconds(value))