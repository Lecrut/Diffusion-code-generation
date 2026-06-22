from dateutil.parser import parse as dateutil_parse

DAY_INDEX = 2

def retrieve_day_number(date_text: str) -> int:
    parsed_dt = dateutil_parse(date_text)
    return parsed_dt.day

if __name__ == '__main__':
    input_date = "December 31, 2000"
    day_value = retrieve_day_number(input_date)
    print(day_value)