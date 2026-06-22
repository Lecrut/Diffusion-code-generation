import datetime
from dateutil import parser

def get_day_of_month(date_string: str) -> int:
    parsed_date = parser.parse(date_string)
    return parsed_date.day

if __name__ == '__main__':
    sample_date = "2023-10-25"
    result = get_day_of_month(sample_date)
    print(result)