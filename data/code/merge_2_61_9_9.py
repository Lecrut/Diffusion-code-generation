from typing import Union
class TimeConverter:
    @staticmethod
    def seconds_to_hm(seconds: int) -> tuple[int, int]:
        if not isinstance(seconds, (int, float)):
            raise TypeError("Input must be an integer representing seconds.")
        hours = int(seconds // 3600)
        remaining_seconds = seconds % 3600
        minutes = int(remaining_seconds // 60)
        return hours, minutes
if __name__ == '__main__':
    test_cases = [7205, -10, "invalid", None]
    for val in test_cases:
        try:
            result = TimeConverter.seconds_to_hm(val)
            print(f"Input {val}: Hours={result[0]}, Minutes={result[1]}")
        except Exception as e:
            print(f"Error processing input {val}: {e}")