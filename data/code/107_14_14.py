from datetime import datetime

def parse_custom_date(date_string: str) -> str:
    try:
        dt = datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")
        return dt.isoformat()
    except ValueError as e:
        raise ValueError(f"Invalid date format: {date_string}") from e

if __name__ == '__main__':
    date_input = "25-12-2023 14:30:00"
    iso_result = parse_custom_date(date_input)
    print(iso_result)