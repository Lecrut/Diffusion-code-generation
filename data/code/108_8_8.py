from dateutil.parser import parse

def get_day_of_month(date_string):
    parsed_date = parse(date_string)
    return parsed_date.day

if __name__ == '__main__':
    sample_date = "2023-10-05"
    print(get_day_of_month(sample_date))