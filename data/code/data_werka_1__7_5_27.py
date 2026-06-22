def convert_seconds(seconds):
    if seconds >= 3600:
        return f"{seconds // 3600} hours"
    elif seconds >= 60:
        return f"{seconds // 60} minutes"
    else:
        return f"{seconds} seconds"

if __name__ == '__main__':
    sample_values = [5, 60, 120, 3600, 7200, 86400]
    for value in sample_values:
        print(convert_seconds(value))