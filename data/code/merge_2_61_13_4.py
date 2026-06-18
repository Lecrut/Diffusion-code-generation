def format_time(seconds):
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    secs = remaining_seconds % 60
    return f"{hours:0>2}:{minutes:02d}:{secs:02d}"
if __name__ == '__main__':
    sample_values = [91543, 86400, 7200]
    for s in sample_values:
        print(format_time(s))