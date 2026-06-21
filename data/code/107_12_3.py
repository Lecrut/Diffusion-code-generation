from datetime import datetime
from calendar import month_abbr

MONTH_MAP = {name: index for index, name in enumerate(month_abbr) if index and name}

def format_date(input_date: str) -> str:
    day_str, month_name, year_str = input_date.split('-')
    month_index = MONTH_MAP[month_name]
    date_obj = datetime(int(year_str), month_index, int(day_str))
    return date_obj.strftime("%Y%m%d")

if __name__ == '__main__':
    original_string = "01-Jan-2024"
    converted_string = format_date(original_string)
    print(converted_string)