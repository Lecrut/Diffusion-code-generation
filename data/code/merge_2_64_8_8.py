import re
from datetime import datetime
def parse_date(date_string: str) -> datetime | None:
    formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%B %d, %Y",
        "%b%d%Y",
        "YYYY-MM-DD",
        "DD/MM/YYYY"
    ]
    for fmt in formats:
        try:
            return datetime.strptime(date_string.strip(), fmt)
        except ValueError:
            continue
    match = re.match(r'^(\d{4})-(\d{2})-(\d{2})$', date_string.replace('/', '-'))
    if match:
        return datetime.strptime(match.group(0), "%Y-%m-%d")
    return None
def format_date_with_full_month(date_obj: datetime) -> str:
    return date_obj.strftime("%B %d, %Y")
if __name__ == '__main__':
    samples = [
        "2023-10-05",
        "05/10/2023",
        "October 5, 2023",
        "Oct052023"
    ]
    for sample in samples:
        parsed = parse_date(sample)
        if parsed is not None:
            print(format_date_with_full_month(parsed))
        else:
            print(f"No valid date found for '{sample}'")