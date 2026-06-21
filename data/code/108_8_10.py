import datetime
from dateutil import parser

REFERENCE_YEAR = 2000
MONTHS_LIST = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def retrieve_day_number(date_text: str) -> int:
    date_obj = parser.parse(date_text)
    return date_obj.day

if __name__ == '__main__':
    test_date = "2000-02-29"
    calculated_day = retrieve_day_number(test_date)
    print(calculated_day)