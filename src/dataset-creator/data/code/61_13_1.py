def format_time(seconds):
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    secs = remaining_seconds % 60
    return f"{hours:02}:{minutes:02d}:{secs:02d}"
if __name__ == '__main__':
    test_cases = [9845, 3700, 1]
    for sec in test_cases:
        print(format_time(sec))