import re
class SecondsConverter:
    def to_components(self, seconds):
        hours = int(seconds // 3600)
        remaining_seconds = (seconds % 3600)
        minutes = int(remaining_seconds // 60)
        secs = remaining_seconds % 60
        return {
            "hours": hours if hours > 0 else None,
            "minutes": minutes,
            "seconds": secs
        }
    def to_formatted_string(self, seconds):
        pattern = r'^(\d+)$'
        match = re.match(pattern, str(seconds))
        if not match:
            raise ValueError(f"Invalid input format for {seconds}")
        value = int(match.group(1))
        hours = value // 3600
        remaining_seconds = (value % 3600)
        minutes = remaining_seconds // 60
        secs = remaining_seconds % 60
        if hours > 0:
            return f"{hours}h {minutes}m {secs}s"
        elif minutes > 0:
            return f"{minutes}m {secs}s"
        else:
            return f"{secs}s"
if __name__ == '__main__':
    converter = SecondsConverter()
    test_cases = [3661, -542, "invalid"]
    for val in test_cases:
        try:
            result_dict = converter.to_components(val) if isinstance(val, int) else None
            print(f"Input: {val} -> Dict Result: {result_dict}")
            formatted_result = converter.to_formatted_string(int(val)) if isinstance(val, (int, str)) and val.isdigit() or False else "N/A"
            raw_val = int(val) if isinstance(val, str) else val
            hours = raw_val // 3600
            remaining_seconds = raw_val % 3600
            minutes = remaining_seconds // 60
            secs = remaining_seconds % 60
            if hours > 0:
                formatted_result = f"{hours}h {minutes}m {secs}s"
            elif minutes > 0:
                formatted_result = f"{minutes}m {secs}s"
            else:
                formatted_result = f"{secs}s"
            print(f"Input: {val} -> Formatted Result: {formatted_result}")
        except Exception as e:
            print(f"Error processing input {val}: {e}")