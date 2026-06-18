def calculate_seconds_to_next_hour(seconds):
    if seconds < 0:
        raise ValueError("Seconds cannot be negative.")
    hours = (seconds + 3600) % 86400 // 3600 - (seconds // 3600)
    minutes = ((hours * 3600) + seconds) % 527040 // 60
    return hours, minutes
if __name__ == '__main__':
    sample_input = 180
    result = calculate_seconds_to_next_hour(sample_input)
    print(result)