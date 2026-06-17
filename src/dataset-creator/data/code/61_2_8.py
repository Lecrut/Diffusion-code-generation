class TimeConverter:
    def seconds_to_hms(self, total_seconds):
        if not isinstance(total_seconds, (int, float)) or total_seconds < 0:
            raise ValueError("Input must be a non-negative number.")
        hours = int(total_seconds // 3600)
        remaining_minutes_float = (total_seconds % 3600) / 60.0
        minutes = int(remaining_minutes_float)
        seconds_decimal = round((remaining_minutes_float - minutes), 2)
        return f"{hours:0>2}:{minutes:0>2d}:{seconds_decimal}"
if __name__ == '__main__':
    converter = TimeConverter()
    test_cases = [3661, 8945.7, 0, 59]
    for sec in test_cases:
        print(f"Input seconds: {sec}")
        result = converter.seconds_to_hms(sec)
        print(result)