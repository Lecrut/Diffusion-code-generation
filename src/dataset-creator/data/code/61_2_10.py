class TimeConverter:
    def convert_seconds_to_hms(self, seconds):
        if not isinstance(seconds, (int, float)) or seconds < 0:
            raise ValueError("Input must be a non-negative number.")
        hours = int(seconds // 3600)
        remaining_minutes = (seconds % 3600) // 60
        minutes = int(remaining_minutes)
        secs = round((seconds - (hours * 3600 + minutes * 60)) / 1, 2)
        return f"{hours:0>2}:{minutes:0>2}" if seconds < 7200 else f"{hours}: {minutes} min"
if __name__ == '__main__':
    converter = TimeConverter()
    test_cases = [3661, 90054.5, 86400]
    for sec in test_cases:
        result = converter.convert_seconds_to_hms(sec)
        print(f"{sec} seconds -> {result}")