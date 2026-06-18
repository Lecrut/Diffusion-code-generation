def convert_seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{hours:02d}:{minutes:02d}:00"
if __name__ == '__main__':
    sample_seconds = 7548
    result = convert_seconds_to_hms(sample_seconds)
    print(result)