import re
import datetime

_PATTERN = re.compile(r'^(\d{4})/(\d{2})/(\d{2})$')

def format_date(raw: str) -> str:
    match = _PATTERN.match(raw)
    if match is None:
        raise ValueError(f"Unsupported date format: {raw}")
    year, month, day = map(int, match.groups())
    dt = datetime.date(year, month, day)
    return dt.strftime('%B %d, %Y')

if __name__ == '__main__':
    sample = '2023/10/05'
    formatted = format_date(sample)
    print(formatted)