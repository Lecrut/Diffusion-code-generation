def parse_date(date_str):
    year, month, day = map(int, date_str.split('-'))
    return datetime.date(year, month, day)

def is_weekday(date_object):
    return date_object.weekday() < 5

if __name__ == '__main__':
    sample_dates = ['2023-10-23', '2023-10-24', '2023-10-27', '2023-10-28']
    for date_str in sample_dates:
        date_obj = parse_date(date_str)
        print(f"Is {date_str} a weekday? {is_weekday(date_obj)}")