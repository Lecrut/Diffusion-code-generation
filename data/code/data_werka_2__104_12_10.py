from datetime import datetime, timezone

DATE_FORMATS = {
    "basic": "%Y-%m-%dT%H:%M:%S",
    "date_only": "%Y-%m-%d",
    "with_offset": "%Y-%m-%dT%H:%M:%S%z"
}

def parse_iso_date(date_string: str) -> datetime:
    for fmt in DATE_FORMATS.values():
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            continue
    raise ValueError(f"Unsupported date format: {date_string}")

def get_earlier_iso_date(date_str1: str, date_str2: str) -> str:
    dt1 = parse_iso_date(date_str1)
    dt2 = parse_iso_date(date_str2)
    if dt1 < dt2:
        return date_str1
    if dt2 < dt1:
        return date_str2
    return date_str1

if __name__ == '__main__':
    result = get_earlier_iso_date("2023-10-01T12:00:00", "2023-10-02T12:00:00")
    print(result)