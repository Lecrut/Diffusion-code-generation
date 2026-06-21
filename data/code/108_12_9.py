from datetime import datetime

DAY_FORMAT = "%Y-%m-%d"
ISO_FORMAT = "%Y-%m-%dT%H:%M:%S"
SAMPLE_TIMESTAMP = "2024-07-04T12:00:00"

def get_day_number(timestamp_str: str) -> int:
    parsed = datetime.strptime(timestamp_str, ISO_FORMAT)
    date_part = parsed.strftime(DAY_FORMAT)
    extracted = datetime.strptime(date_part, DAY_FORMAT)
    return extracted.day

if __name__ == '__main__':
    result = get_day_number(SAMPLE_TIMESTAMP)
    print(result)