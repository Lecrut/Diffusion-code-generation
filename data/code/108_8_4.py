from dateutil import parser

def parse_date_and_get_day(date_string):
    parsed_date = parser.parse(date_string)
    return parsed_date.day

if __name__ == '__main__':
    sample_date = '2023-10-05'
    day_of_month = parse_date_and_get_day(sample_date)
    print(day_of_month)