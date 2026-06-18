def convert_seconds_to_hm(seconds):
    if seconds < 0:
        raise ValueError("Seconds must be non-negative.")
    hours = seconds // 3600
    remaining_after_hours = seconds % 3600
    minutes = remaining_after_hours // 60
    return hours, minutes
if __name__ == '__main__':
    sample_seconds = 7215
    h, m = convert_seconds_to_hm(sample_seconds)
    print(f"{h} hours and {m} minutes")