from dateutil.parser import parse

def get_day_of_month(date_str):
    parsed_date = parse(date_str)
    return parsed_date.day

if __name__ == '__main__':
    sample_date_str = "2023-11-15T09:45:00"
    day_of_month = get_day_of_month(sample_date_str)
    print(day_of_month)