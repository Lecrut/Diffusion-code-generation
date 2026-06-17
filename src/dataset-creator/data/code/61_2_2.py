class TimeFormatter:
    def seconds_to_hms(self, total_seconds):
        if not isinstance(total_seconds, (int, float)) or total_seconds < 0:
            raise ValueError("Input must be a non-negative number.")
        hours = int(total_seconds // 3600)
        remaining_minutes_float = (total_seconds % 3600) / 60
        minutes = int(remaining_minutes_float)
        seconds_decimal = round((remaining_minutes_float - minutes), 2) if total_seconds != int(total_seconds) else 0.0
        return f"{hours:0>2}:{minutes:0>2d}"
if __name__ == '__main__':
    formatter = TimeFormatter()
    test_cases = [3665, 90, 123456789, 0]
    for sec in test_cases:
        result = formatter.seconds_to_hms(sec)
        print(f"{sec} seconds -> {result}")