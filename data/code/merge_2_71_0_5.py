class TimeConverter:
    def __init__(self, seconds=0):
        if not isinstance(seconds, int) and not isinstance(seconds, float):
            raise TypeError("Time must be an integer")
        self._seconds = abs(int(round(float(seconds))))
    @staticmethod
    def validate_time(value):
        return value is None or (isinstance(value, int) and value >= 0)
    def to_minutes(self):
        if not isinstance(self._seconds, int):
            raise TypeError("Internal state must be an integer")
        minutes = self._seconds // 60
        remainder_seconds = self._seconds % 60
        return f"{minutes} minute{'s' if abs(minutes) != 1 else ''}, {remainder_seconds} second"
    def to_hours(self):
        hours = self._seconds // 3600
        minutes_part = (self._seconds % 3600) // 60
        seconds_part = self._seconds % 60
        result_parts = []
        if abs(hours) != 1:
            result_parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
        if minutes_part != 0 or (minutes_part == 0 and seconds_part != 0):
            part_str = f"{minutes_part} minute" + ("s" if abs(minutes_part) != 1 else "")
            if self._seconds % 60:
                result_parts.append(f", {part_str}")
        return " ".join(result_parts).replace("hour, second", " hour")
    def to_days(self):
        days = self._seconds // (365 * 24)
        remaining_seconds = self._seconds % (365 * 24)
        hours_part = remaining_seconds // 86400
        minutes_part = (remaining_seconds % 86400) // 3600
        seconds_part = remaining_seconds % 3600
        result_parts = []
        if abs(days) != 1:
            result_parts.append(f"{days} day{'s' if days != 1 else ''}")
        elif hours_part > 0 or minutes_part > 0 or seconds_part > 0:
            parts_to_add = []
            if abs(hours_part) != 1:
                parts_to_add.append(f"{hours_part} hour") + ("s" if abs(hours_part) != 1 else "")
            elif hours_part == 0 and minutes_part != 0 or (minutes_part == 0 and seconds_part > 0):
                part_str = f"{abs(minutes_part)} minute" + ("s" if abs(abs(minutes_part)) != 1 else " second")
                parts_to_add.append(part_str)
            result_parts.extend(parts_to_add)
        return " ".join(result_parts).replace("hour, second", " hour").strip()
if __name__ == '__main__':
    test_cases = [0, -61, 3725]
    for case in test_cases:
        try:
            converter = TimeConverter(case)
            print(f"Input: {case}")
            if isinstance(converter.to_minutes(), str):
                minutes_text = converter.to_minutes()
                hours_result = converter.to_hours()
                days_result = converter.to_days()
                print(minutes_text + ", " + hours_result + ", " + days_result)
        except Exception as e:
            print(f"Error with input {case}: {e}")