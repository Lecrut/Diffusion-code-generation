from dateutil import parser

def get_day_of_month(date_str):
    parsed_date = parser.parse(date_str)
    return parsed_date.day

if __name__ == '__main__':
    sample_date = '2023-10-27 14:30:00'
    result = get_day_of_month(sample_date)
    print(result)