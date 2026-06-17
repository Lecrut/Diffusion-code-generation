def convert_seconds_to_hm(seconds):
    if seconds < 0:
        return None
    hours = seconds // 3600
    remaining_after_hours = seconds % 3600
    minutes = remaining_after_hours // 60
    return f"{hours}h {minutes}m"
if __name__ == '__main__':
    sample_seconds = 7265
    result = convert_seconds_to_hm(sample_seconds)
    print(result)