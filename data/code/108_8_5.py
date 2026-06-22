import datetime
from dateutil import parser

def get_day_of_month(date_string: str) -> int:
    parsed_date = parser.parse(date_string)
    return parsed_date.day

if __name__ == '__main__':
    date_str = "2023-10-15"
    result = get_day_of_month(date_str)
    print(result)