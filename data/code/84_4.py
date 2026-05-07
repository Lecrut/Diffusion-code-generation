from datetime import datetime
def get_day_of_year(date_string):
    try:
        date_object = datetime.strptime(date_string, '%Y-%m-%d')
        return date_object.timetuple().tm_yday
    except ValueError:
        return None
if __name__ == '__main__':
    test_dates = [
        '2023-10-27',
        '2024-01-01',
        '1999-12-31',
        '2023-02-29',
        'invalid-date'
    ]
    for date_str in test_dates:
        day_num = get_day_of_year(date_str)
        print(f"Date: {date_str}, Day of Year: {day_num}")