class TimeFormatter:
    def convert_seconds_to_hm(self, seconds):
        if not isinstance(seconds, (int, float)) or seconds < 0:
            raise ValueError("Input must be a non-negative number.")
        hours = int(seconds // 3600)
        remaining_minutes_float = (seconds % 3600) / 60
        minutes = int(remaining_minutes_float)
        total_seconds_in_minute = seconds - (hours * 3600 + minutes * 60)
        return f"{hours:02d}:{minutes:02d}.{total_seconds_in_minute:.1f}"
if __name__ == '__main__':
    formatter = TimeFormatter()
    test_cases = [
        0,
        3599,
        7260,
        86400,
        1.5,
        3661.25
    ]
    for sec in test_cases:
        print(f"{sec} seconds -> {formatter.convert_seconds_to_hm(sec)}")