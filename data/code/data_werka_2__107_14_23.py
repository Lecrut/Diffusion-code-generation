from datetime import datetime

INPUT_FMT = "%d-%m-%Y %H:%M:%S"
OUTPUT_FMT = "%Y-%m-%dT%H:%M:%S"

def to_iso8601(source: str) -> str:
    if not isinstance(source, str):
        raise ValueError("Expected a string")
    try:
        parsed = datetime.strptime(source, INPUT_FMT)
    except ValueError:
        raise ValueError("Invalid date format")
    return parsed.strftime(OUTPUT_FMT)

if __name__ == '__main__':
    raw = "15-08-2022 09:15:30"
    iso_val = to_iso8601(raw)
    print(iso_val)