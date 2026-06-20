from dateutil import parser

DATE_FORMAT = "%Y-%m-%d"

def extract_day_of_month(date_string):
    date_object = parser.parse(date_string)
    return date_object.day

if __name__ == '__main__':
    sample_date_str = "2023-10-27"
    day_of_month = extract_day_of_month(sample_date_str)
    print(day_of_month)