from dateutil import parser

def get_day_of_week(date_str):
    date_obj = parser.parse(date_str)
    return date_obj.strftime('%A')

if __name__ == '__main__':
    sample_date = 'December 25, 2023'
    day_of_week = get_day_of_week(sample_date)
    print(day_of_week)