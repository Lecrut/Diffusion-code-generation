from datetime import datetime

def parse_day_from_iso(timestamp: str) -> int:
    try:
        dt = datetime.fromisoformat(timestamp)
    except ValueError as e:
        raise ValueError(f"Invalid timestamp format: {timestamp}") from e
    return dt.day

if __name__ == '__main__':
    sample_timestamp = '2024-07-04T12:00:00'
    result = parse_day_from_iso(sample_timestamp)
    print(result)