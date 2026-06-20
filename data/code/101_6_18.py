from dateutil import parser

def get_day_of_week(date_str):
    parsed_date = parser.parse(date_str)
    return parsed_date.strftime('%A')

if __name__ == '__main__':
    sample_date = 'February 14, 2023'
    day_of_week = get_day_of_week(sample_date)
    print(day_of_week)