import datetime
def parse_and_get_weekday(date_str: str) -> str:
    formats = [
        "%Y-%m-%d",
        "%B %d, %Y",
        "%d/%m/%Y",
        "%Y.%m.%d",
        "January 15, 2024"
    ]
    for fmt in formats:
        try:
            return datetime.datetime.strptime(date_str, fmt).strftime("%A")
        except ValueError:
            continue
    raise ValueError(f"No recognized format found for date string: {date_str}")
if __name__ == '__main__':
    samples = [
        "2024-12-31",
        "December 31, 2024",
        "31/12/2024",
        "2024.12.31"
    ]
    for sample in samples:
        try:
            result = parse_and_get_weekday(sample)
            print(f"{sample} -> {result}")
        except ValueError as e:
            print(f"Error parsing '{sample}': {e}")