class TimeFormatter:
    def seconds_to_hms(self, total_seconds):
        if not isinstance(total_seconds, (int, float)) or total_seconds < 0:
            raise ValueError("Input must be a non-negative number.")
        hours = int(total_seconds // 3600)
        remaining_minutes = (total_seconds % 3600) // 60
        minutes = int(remaining_minutes)
        seconds_decimal = total_seconds - (hours * 3600 + minutes * 60)
        return f"{hours:02}:{minutes:02}.{seconds_decimal:.1f}"
if __name__ == '__main__':
    test_cases = [
        945,
        8639.5,
        0,
        7265.25
    ]
    formatter = TimeFormatter()
    for sec in test_cases:
        result = formatter.seconds_to_hms(sec)
        print(f"{sec} seconds -> {result}")