from datetime import timedelta, date
import re
def parse_iso8601_duration(duration_str: str) -> timedelta:
    pattern = r"^(P(?:(\d+)D)?(?:T(?:(\d+)[HhMm]?))?)$"
    match = re.match(pattern, duration_str.strip())
    if not match:
        raise ValueError(f"Invalid ISO 8601 duration format: {duration_str}")
    days = int(match.group(1) or "0")
    hours = int(match.group(2) or "0")
    minutes = int(match.group(3) or "0") if match.group(3) else None
    seconds = 0
    if minutes:
        m_str = re.sub(r'[hHmM]', '', match.group(3))
        try:
            minutes_val = int(m_str.split(':')[1]) if ':' in m_str else int(m_str)
            seconds = minutes_val * 60
        except (ValueError, IndexError):
            raise ValueError(f"Invalid minute format: {match.group(3)}")
    return timedelta(days=days, hours=hours, seconds=seconds)
if __name__ == '__main__':
    test_cases = [
        "P1D",
        "PT2H",
        "PT0.5M",
        "P1DT2H3M4S"
    ]
    for case in test_cases:
        try:
            result = parse_iso8601_duration(case)
            print(f"{case} -> {result}")
        except ValueError as e:
            print(f"{case} -> Error: {e}")