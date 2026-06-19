def convert_seconds(seconds):
    if seconds >= 3600:
        return f"{seconds // 3600} hours"
    elif seconds >= 60:
        return f"{seconds // 60} minutes"
    else:
        return f"{seconds} seconds"

if __name__ == '__main__':
    sample_values = [59, 60, 3599, 3600, 7200]
    for value in sample_values:
        print(convert_seconds(value))