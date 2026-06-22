def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{remaining_seconds:02d}"

if __name__ == '__main__':
    print(seconds_to_hms(3661))
    print(seconds_to_hms(7322))