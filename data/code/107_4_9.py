from datetime import datetime

DATE_INPUT_FORMAT = "%d.%m.%Y"
DATE_OUTPUT_FORMAT = "%Y-%m-%d"

def validate_date_string(date_str: str) -> bool:
    if not isinstance(date_str, str):
        return False
    parts = date_str.split(".")
    if len(parts) != 3:
        return False
    if any(len(part) != 2 for part in parts[:2]):
        return False
    if len(parts[2]) != 4:
        return False
    if not all(part.isdigit() for part in parts):
        return False
    return True

def transform_date(date_str: str) -> str:
    if not validate_date_string(date_str):
        raise ValueError(f"Unsupported date format: {date_str}")
    dt = datetime.strptime(date_str, DATE_INPUT_FORMAT)
    return dt.strftime(DATE_OUTPUT_FORMAT)

if __name__ == '__main__':
    samples = ["25.12.2023", "01.01.2000", "31.12.1999", "15.08.2021"]
    for sample in samples:
        result = transform_date(sample)
        print(result)