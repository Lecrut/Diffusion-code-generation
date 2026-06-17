import time
class TimeConverter:
    @staticmethod
    def seconds_to_hm(seconds):
        if not isinstance(seconds, (int, float)):
            raise TypeError("Input must be an integer or float representing seconds.")
        try:
            total_seconds = int(float(seconds))                                                                 
            if total_seconds < 0:
                raise ValueError("Seconds cannot be negative.")
            hours = total_seconds // 3600
            remaining_minutes = (total_seconds % 3600) // 60
            return {
                "hours": int(hours),
                "minutes": int(remaining_minutes),
                "seconds_remaining": total_seconds % 60
            }
        except OverflowError:
            raise ValueError("Input value is too large to be converted.")
if __name__ == '__main__':
    sample_values = [3665, -10, "invalid", None]
    for val in sample_values:
        try:
            result = TimeConverter.seconds_to_hm(val)
            print(f"Input {val}: Hours={result['hours']}, Minutes={result['minutes']}")
        except (TypeError, ValueError) as e:
            print(f"Error processing input {val}: {e}")