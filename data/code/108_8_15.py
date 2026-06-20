from dateutil import parser

def extract_day_of_month(date_string):
    parsed_date = parser.parse(date_string)
    return parsed_date.day

if __name__ == '__main__':
    sample_date = "2023-10-27T14:30:00"
    result = extract_day_of_month(sample_date)
    print(result)