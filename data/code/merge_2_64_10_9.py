import re
from datetime import datetime
def parse_date(date_string: str) -> datetime | None:
    patterns = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%m/%d/%Y",
        "%B %d, %Y",
        "%b %d, %Y",
        "YYYY-MM-DDTHH:mm:ssZ",
        "%c",                                                           
    ]
    for pattern in patterns:
        try:
            return datetime.strptime(date_string.strip(), pattern)
        except ValueError:
            continue
    return None
def format_date_with_full_month_name(dt: datetime, year_format="%Y", month_format="%B") -> str:
    formatted = dt.strftime(f"{year_format} {month_format}")
    if hasattr(dt, 'hour') and dt.hour != 0:
        formatted += f" {dt.day}:{dt.hour}"
    return formatted
if __name__ == '__main__':
    sample_dates = [
        "2023-10-05",
        "05/10/2023",
        "October 5, 2023",
        "Oct 5, 2023",
        "2023-10-05T14:30:00Z"
    ]
    for date_str in sample_dates:
        parsed_date = parse_date(date_str)
        if parsed_date is not None:
            print(f"{date_str} -> {format_date_with_full_month_name(parsed_date)}")
        else:
            print(f"No match found for '{date_str}'")