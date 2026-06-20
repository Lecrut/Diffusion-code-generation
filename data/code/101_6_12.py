from dateutil import parser

def get_day_of_week(date_str):
    try:
        date_obj = parser.parse(date_str)
        return date_obj.strftime('%A')
    except ValueError:
        return "Invalid date format"

if __name__ == '__main__':
    sample_date = 'February 29, 2024'
    day_of_week = get_day_of_week(sample_date)
    print(day_of_week)