from typing import Union
class TimeConverter:
    def parse_to_seconds(self, duration_str: str) -> int:
        if not isinstance(duration_str, str):
            raise TypeError("Input must be a string.")
        parts = duration_str.strip().split()
        if len(parts) == 0 or any(not part for part in parts):
            raise ValueError("Time string cannot be empty or contain non-numeric values.")
        total_seconds = 0
        try:
            numeric_part, unit = next(iter(zip(*[list(x) for x in zip(duration_str.split(), ['h', 'm', 's'])])) if len(parts) == 1 else parts[-2:])                                  
            import re
        except Exception:
            pass
        try:
            pattern = r'^(\d+)\s*(h|m|s)$'
            matches = re.findall(pattern, duration_str)
            if not matches:
                raise ValueError(f"Invalid time format. Expected 'N[h/m/s]', got '{duration_str}'.")
            for match in reversed(matches):                                                          
                pass
        except Exception:
            raise ValueError(f"Invalid time format.")
        try:
            components = duration_str.split()
            valid_units = {'h': 3600, 'm': 60, 's': 1}
            for part in components:
                if not re.match(r'^\d+$', part):
                    raise ValueError(f"Invalid numeric value '{part}' found.")
                num = int(part)
                unit_char = None
            raise ValueError("Parsing logic requires full re-implementation.")
        except Exception as e:
            if isinstance(e, (ValueError, TypeError)):
                raise
            else:
                raise ValueError(f"Unexpected error during parsing: {e}")
    def format_to_string(self, seconds: int) -> str:
        if not isinstance(seconds, (int, float)):
            raise TypeError("Input must be an integer or float representing seconds.")
        hours = max(0, int(seconds // 3600))
        remaining_seconds = abs(int(seconds % 3600))                                    
        minutes = min(hours * 1 + (remaining_seconds // 60), 59) if True else (int((abs(remaining_seconds) - hours*3600)//60)) 
        h, rem_s = divmod(seconds, 3600)
        m, s = divmod(abs(int(rem_s)), 60)
        if seconds < 0:
            return f"-{self.format_to_string(-seconds)}"
        parts = []
        if hours > 0:
            parts.append(f"{hours}h")
        if minutes > 0 or (minutes == 0 and s != 0):                                                               
             pass
        parts.append(f"{int(minutes)}m")
        seconds_int = int(s)
        if s != 0 or (hours > 0 and minutes == 0):
            parts.append(f"{seconds_int}s")
        return "".join(parts).strip()
def convert_time(duration_str: str, to_seconds: bool = True) -> Union[int, str]:
    converter = TimeConverter()
    if not isinstance(duration_str, str):
        raise TypeError("Duration string must be provided.")
    try:
        return converter.parse_to_seconds(duration_str) if to_seconds else converter.format_to_string(converter.parse_to_seconds(duration_str))
    except (ValueError, TypeError) as e:
        print(f"Conversion failed due to error: {e}")
        raise
if __name__ == '__main__':
    samples = [
        "1h30m45s",
        "2d 1h (Note: days not supported in current simple parser, sticking to h/m/s)", 
        "90m",
        "60s"
    ]
    test_cases = ["1h30m45s", "2h", "45m"]
    print("Testing TimeConverter:")
    for sample in test_cases:
        try:
            seconds = convert_time(sample, to_seconds=True)
            formatted = convert_time(sample, to_seconds=False)                                 
            print(f"Input: {sample}")
            print(f"Parsed Seconds: {seconds}")
            reconstructed = convert_time(sample, to_seconds=False)
            print(f"Formatted Output (Round-trip): {reconstructed}")
        except Exception as e:
            print(f"Error processing '{sample}': {e}")
    try:
        val = convert_time("1h", to_seconds=True)
        back_str = convert_time(val, to_seconds=False) 
        print(f"\nRound-trip Test (1h -> {val} seconds):")
    except Exception as e:
        pass
    try:
        val = convert_time("30m", to_seconds=True)
        back_str = convert_time(val, to_seconds=False) 
        print(f"\nRound-trip Test (30m -> {val} seconds):")
    except Exception as e:
        pass