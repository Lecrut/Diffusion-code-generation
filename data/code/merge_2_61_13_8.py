def format_time(seconds: int) -> str:
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    secs = remaining_seconds % 60
    return f"{hours}:{minutes:02d}:{secs:02d}"
if __name__ == '__main__':
    sample_time = 97158
    print(format_time(sample_time))