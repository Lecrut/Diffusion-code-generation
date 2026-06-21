from datetime import datetime
from typing import Final

ISO_FORMAT: Final[str] = "%Y-%m-%dT%H:%M:%S"
SAMPLE_TIMESTAMP: Final[str] = "2024-07-04T12:00:00"

def extract_day_component(timestamp_str: str) -> int:
    parsed_date = datetime.strptime(timestamp_str, ISO_FORMAT)
    return parsed_date.day

if __name__ == '__main__':
    result = extract_day_component(SAMPLE_TIMESTAMP)
    print(result)