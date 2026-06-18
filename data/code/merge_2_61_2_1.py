class TimeFormatter:
    def convert_seconds_to_hms(self, seconds):
        if not isinstance(seconds, (int, float)) or seconds < 0:
            raise ValueError("Input must be a non-negative number.")
        hours = int(seconds // 3600)
        remaining_minutes = (seconds % 3600) // 60
        minutes = int(remaining_minutes)
        secs = round((seconds - (hours * 3600 + minutes * 60)) / 1, 2) if seconds != int(seconds) else "0"
        return f"{hours:0>2}:{minutes:0>2}"
if __name__ == '__main__':
    formatter = TimeFormatter()
    test_cases = [3754, 86399, 1000.5]
    for sec in test_cases:
        result = formatter.convert_seconds_to_hms(sec)
        print(f"{sec} seconds -> {result}")