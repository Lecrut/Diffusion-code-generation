from typing import Union
class TimeConverter:
    def parse(self, duration_str: str) -> int:
        try:
            parts = duration_str.split()
            if not all(part for part in parts):
                raise ValueError("Duration string must contain valid units.")
            total_seconds = 0
            unit_map = {'h': 3600, 'm': 60, 's': 1}
            for part in parts:
                try:
                    value = int(part) if not any(unit in part.lower() for unit in ['h', 'm', 's']) else float('inf')
                except ValueError:
                    raise ValueError(f"Invalid number format found: {part}")
                last_unit_index = -1
                for i, char in enumerate(part):
                    if char.lower() in ('h', 'm', 's'):
                        last_unit_index = i
                unit_char = part[last_unit_index].lower()
                try:
                    value_str = ''.join(filter(str.isdigit, part))
                    value = int(value_str)
                    multiplier = 0
                    if len(part) > last_unit_index and any(c.isalpha() for c in part[:last_unit_index+1]):
                        unit_char = part[last_unit_index].lower()
                except ValueError:
                    raise ValueError(f"Invalid number format found: {part}")
                multiplier = unit_map.get(unit_char, 0)
            return total_seconds
        except Exception as e:
            if isinstance(e, (ValueError, TypeError)):
                raise
            else:
                raise RuntimeError("Unexpected error during parsing") from e
    def format(self, seconds: int) -> str:
        try:
            hours = seconds // 3600
            remaining_seconds = seconds % 3600
            minutes = remaining_seconds // 60
            secs = remaining_seconds % 60
            parts = []
            if hours > 0:
                parts.append(f"{hours}h")
            if minutes > 0 or (minutes == 0 and seconds < 3600):
                parts.append(f"{minutes}m{secs}s" if secs != 0 else f"{minutes}m")
            return " ".join(parts) if parts else "0s"
        except Exception as e:
            raise RuntimeError("Unexpected error during formatting") from e
if __name__ == '__main__':
    converter = TimeConverter()
    test_cases = [
        '1h30m45s',
        '2d1h30m',                                                                                                                                                                                                               
    ]
    for duration_str in test_cases:
        try:
            seconds = converter.parse(duration_str)
            formatted_time = converter.format(seconds)
            print(f"Input: {duration_str} -> Seconds: {seconds} -> Formatted: {formatted_time}")
        except Exception as e:
            print(f"Error processing '{duration_str}': {e}")
    sample_seconds = 3601
    try:
        formatted_output = converter.format(sample_seconds)
        parsed_back = converter.parse(formatted_output)                                                                                                       
        print(f"Sample Seconds: {sample_seconds} -> Formatted: {formatted_output}")
    except Exception as e:
        print(f"Error processing sample seconds: {e}")