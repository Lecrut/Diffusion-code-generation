import datetime
from dateutil import parser

REFERENCE_YEAR = 2000
DATE_FORMAT_STR = "%B %d, %Y"

def retrieve_day_component(date_input: str) -> int:
    parsed_datetime = parser.parse(date_input)
    return parsed_datetime.day

if __name__ == '__main__':
    sample_date = "December 25, 2023"
    day_value = retrieve_day_component(sample_date)
    print(day_value)