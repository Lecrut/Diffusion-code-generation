from datetime import datetime
from calendar import month_abbr

MONTH_ABBREVIATIONS: dict[str, int] = {
    name: index for index, name in enumerate(month_abbr) if index
}

DAY_WIDTH: int = 2
YEAR_WIDTH: int = 4
SEPARATOR: str = "-"

def format_date(input_date: str) -> str:
    day_str, month_name, year_str = input_date.split(SEPARATOR)
    month_index = MONTH_ABBREVIATIONS[month_name]
    date_obj = datetime(int(year_str), month_index, int(day_str))
    return date_obj.strftime("%Y%m%d")

if __name__ == '__main__':
    original_string = "01-Jan-2024"
    converted_string = format_date(original_string)
    print(converted_string)