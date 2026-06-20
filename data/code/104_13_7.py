from datetime import datetime

def parse_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d')

def get_week_number(date):
    return date.isocalendar()[1]

def dates_in_same_week(date1_str, date2_str):
    date1 = parse_date(date1_str)
    date2 = parse_date(date2_str)
    return get_week_number(date1) == get_week_number(date2)

if __name__ == '__main__':
    print(dates_in_same_week('2023-10-01', '2023-10-07'))
    print(dates_in_same_week('2023-10-01', '2023-10-08'))