from dateutil.parser import parse

def extract_day(date_input: str) -> int:
    dt = parse(date_input)
    return dt.day

if __name__ == '__main__':
    test_string = "July 4, 1776"
    day_number = extract_day(test_string)
    print(day_number)