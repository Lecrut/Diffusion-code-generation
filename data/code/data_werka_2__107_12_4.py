from datetime import datetime
from typing import Optional

MONTH_ABBREVIATIONS: dict[str, int] = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
    "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
    "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
}

def transform_date(raw_date: str) -> str:
    if not isinstance(raw_date, str):
        raise ValueError("Input must be a string")
    
    parts = raw_date.split("-")
    if len(parts) != 3:
        raise ValueError("Date string must be in DD-Mon-YYYY format")
    
    day_str, month_str, year_str = parts
    
    month_num = MONTH_ABBREVIATIONS.get(month_str)
    if month_num is None:
        raise ValueError(f"Unsupported month abbreviation: {month_str}")
    
    day = int(day_str)
    year = int(year_str)
    
    date_obj = datetime(year, month_num, day)
    return date_obj.strftime("%Y%m%d")

if __name__ == '__main__':
    input_date: str = "15-Oct-2021"
    formatted_date: str = transform_date(input_date)
    print(formatted_date)