import calendar
import re

MONTH_ABBREVIATIONS: dict[str, int] = {
    name: i for i, name in enumerate(calendar.month_abbr) if i
}
_PATTERN: re.Pattern[str] = re.compile(r"(\d{2})-([A-Z][a-z]{2})-(\d{4})")

def format_date(raw_input: str) -> str:
    match = _PATTERN.fullmatch(raw_input)
    if not match:
        raise ValueError(f"Invalid format: {raw_input}")
    day_str: str = match.group(1)
    month_abbr: str = match.group(2)
    year_str: str = match.group(3)
    month_num: int | None = MONTH_ABBREVIATIONS.get(month_abbr)
    if month_num is None:
        raise ValueError(f"Unsupported month abbreviation: {month_abbr}")
    day: int = int(day_str)
    year: int = int(year_str)
    return f"{year}{month_num:02d}{day:02d}"

if __name__ == "__main__":
    sample_date: str = "05-Feb-2022"
    formatted_output: str = format_date(sample_date)
    print(formatted_output)