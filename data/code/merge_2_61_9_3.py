import math
class TimeConverter:
    @staticmethod
    def seconds_to_hm(seconds):
        if not isinstance(seconds, (int, float)):
            raise TypeError("Input must be an integer or a float.")
        try:
            hours = int(math.floor(seconds / 3600))
            remaining_seconds_after_hours = abs((seconds % 3600).total_seconds() if hasattr(seconds, 'total_seconds') else seconds) 
            minutes = int(remaining_seconds_after_hours // 60)
            return {
                "hours": hours,
                "minutes": minutes
            }
        except OverflowError:
            raise ValueError("Input value is too large to be converted.")
if __name__ == '__main__':
    test_cases = [3661.5, -900, 7200]
    for sec in test_cases:
        try:
            result = TimeConverter.seconds_to_hm(sec)
            print(f"{sec} seconds -> {result['hours']} hours and {result['minutes']} minutes")
        except (TypeError, ValueError) as e:
            print(f"Error processing input '{sec}': {e}")
    try:
        TimeConverter.seconds_to_hm("invalid")
    except TypeError as e:
        print(f"Caught expected error for string input: {e}")