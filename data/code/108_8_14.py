from dateutil import parser

def get_day_of_month(date_string):
    date = parser.parse(date_string)
    return date.day

if __name__ == '__main__':
    sample_date = "2023-10-05"
    print(get_day_of_month(sample_date))