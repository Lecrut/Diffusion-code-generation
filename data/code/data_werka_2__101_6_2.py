from dateutil.parser import parse

def get_day_of_week(date_string):
    parsed_date = parse(date_string)
    return parsed_date.strftime('%A')

if __name__ == '__main__':
    result = get_day_of_week('January 15, 2023')
    print(result)