from dateutil.parser import parse

def get_day_of_week(date_str):
    date_obj = parse(date_str)
    return date_obj.strftime('%A')

if __name__ == '__main__':
    sample_date = 'January 15, 2023'
    print(get_day_of_week(sample_date))