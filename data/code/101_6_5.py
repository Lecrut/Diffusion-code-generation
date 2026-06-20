from dateutil import parser

def get_day_of_week(date_str):
    return parser.parse(date_str).strftime('%A')

if __name__ == '__main__':
    sample_date = 'January 15, 2023'
    print(get_day_of_week(sample_date))