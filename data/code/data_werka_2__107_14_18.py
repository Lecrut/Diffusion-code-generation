from datetime import datetime

def parse_to_iso8601(date_string: str) -> str:
    try:
        parsed = datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")
    except ValueError as e:
        raise ValueError(f"Invalid date format: {date_string}") from e
    return parsed.strftime("%Y-%m-%dT%H:%M:%S")

if __name__ == '__main__':
    sample_date = "15-08-2024 09:15:30"
    iso_result = parse_to_iso8601(sample_date)
    print(iso_result)