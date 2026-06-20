class TimeConverter:
    @staticmethod
    def split_time_str(time_str):
        return list(map(int, time_str.split(':')))

    @staticmethod
    def validate_time_components(h, m, s):
        if not (0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59):
            raise ValueError("Time components out of valid range")

    @classmethod
    def time_to_minutes(cls, time_str):
        try:
            h, m, s = cls.split_time_str(time_str)
            cls.validate_time_components(h, m, s)
            total_minutes = h * 60 + m + (s / 60.0)
            return total_minutes
        except ValueError as e:
            raise ValueError(f"Invalid time format. Expected HH:MM:SS. Error: {e}")

if __name__ == '__main__':
    test_cases = [
        ("00:00:00", 0),
        ("23:59:59", 1439.9833333333334),
        ("01:30:00", 90)
    ]
    
    for time_str, expected in test_cases:
        try:
            result = TimeConverter.time_to_minutes(time_str)
            print(f"time_to_minutes('{time_str}') returned {result}, expected {expected}")
        except ValueError as e:
            print(e)