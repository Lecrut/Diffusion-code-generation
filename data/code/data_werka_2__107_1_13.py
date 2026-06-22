from datetime import datetime
from typing import Tuple

FORMAT_INPUT = '%m/%d/%Y'
FORMAT_OUTPUT = '%d-%m-%Y'

def parse_date_string(date_str: str) -> Tuple[int, int, int]:
    parts = date_str.split('/')
    if len(parts) != 3:
        raise ValueError("Expected MM/DD/YYYY format")
    month, day, year = parts
    return int(month), int(day), int(year)

def format_date_components(year: int, month: int, day: int) -> str:
    date_obj = datetime(year=year, month=month, day=day)
    return date_obj.strftime(FORMAT_OUTPUT)

def convert_date(date_str: str) -> str:
    month, day, year = parse_date_string(date_str)
    return format_date_components(year, month, day)

if __name__ == '__main__':
    sample_input = '07/04/1776'
    converted = convert_date(sample_input)
    print(converted)