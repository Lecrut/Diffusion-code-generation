from dateutil import parser

def extract_day_of_month(date_string):
    parsed_date = parser.parse(date_string)
    return parsed_date.day

if __name__ == '__main__':
    sample_date_str = "2023-11-05T12:45:30Z"
    day_of_month = extract_day_of_month(sample_date_str)
    print(day_of_month)