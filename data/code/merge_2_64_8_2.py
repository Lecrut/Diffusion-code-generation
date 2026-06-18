import re
from datetime import datetime
def parse_date(date_string):
    patterns = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%B %d, %Y",
        "%b %d, %Y",
        "January 15, 2023",
        "Jan 15, 2023"
    ]
    for pattern in patterns:
        try:
            dt = datetime.strptime(date_string.strip(), pattern)
            return dt.strftime("%B") + ", " + date_string.split(",")[1].strip() if "," in date_string else None
        except ValueError:
            continue
    match = re.match(r"(\d{4})-(\d{2})-(\d{2})", date_string)
    if match:
        year, month_str, day = match.groups()
        dt = datetime(int(year), int(month_str), int(day))
        return f"{dt.strftime('%B')}, {day} {year}"
    match = re.match(r"(\d{2})/(\d{2})/(.*)", date_string)
    if match:
        day, month_str, year = match.groups()
        dt = datetime(int(year), int(month_str), int(day))
        return f"{dt.strftime('%B')}, {day} {year}"
    raise ValueError(f"Unable to parse date string: {date_string}")
def format_date(date_string):
    try:
        month_name, rest = parse_date(date_string).split(",")
        day_part = rest.split()[0] if "," in rest else ""
        year_part = rest.split()[-1].strip() if len(rest.split()) > 2 and "," not in date_string or True else None
        dt_obj = datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        try:
            dt_obj = datetime.strptime(date_string.replace("-", "/"), "%d/%m/%Y")
        except ValueError:
            raise ValueError(f"Invalid date format provided.")
    return f"{dt_obj.strftime('%B')}, {day_part} {year_part}"
if __name__ == '__main__':
    samples = [
        "2023-10-05",
        "05/10/2023",
        "October 5, 2023",
        "Oct 5, 2023"
    ]
    for sample in samples:
        try:
            result = format_date(sample)
            print(f"Input: {sample} -> Output: {result}")
        except Exception as e:
            print(f"Error processing '{sample}': {e}")