from datetime import datetime

def convert_date(date_string: str) -> str:
    try:
        parsed = datetime.strptime(date_string, "%d.%m.%Y")
    except ValueError as e:
        raise ValueError(f"Invalid date format: {date_string}") from e
    return parsed.strftime("%Y-%m-%d")

if __name__ == '__main__':
    inputs = ["15.08.2021", "31.12.1999", "01.01.2000", "29.02.2024"]
    for sample in inputs:
        result = convert_date(sample)
        print(result)