import datetime

def sort_iso8601_dates(date_strings):
    if not date_strings:
        return []
    
    def validate_and_convert(date_str):
        if not isinstance(date_str, str):
            raise ValueError(f"Expected string, got {type(date_str).__name__}")
        if not date_str:
            raise ValueError("Empty date string")
        try:
            dt = datetime.datetime.fromisoformat(date_str)
            return dt.timestamp()
        except ValueError:
            raise ValueError(f"Invalid ISO 8601 format: {date_str}")

    timestamp_map = {}
    for d in date_strings:
        ts = validate_and_convert(d)
        timestamp_map[d] = ts
    
    sorted_dates = sorted(date_strings, key=lambda x: timestamp_map[x])
    return sorted_dates

if __name__ == '__main__':
    sample_dates = [
        "2023-10-01T12:00:00",
        "2021-05-15T08:30:00",
        "2023-01-20T18:45:00",
        "2022-12-31T23:59:59",
        "2020-02-29T00:00:00"
    ]
    result = sort_iso8601_dates(sample_dates)
    print(result)