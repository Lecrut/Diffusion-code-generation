import datetime

YEAR_ADDITION = 1
DAY_ADDITION = 1

def add_year_and_day(date_str):
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    new_date_obj = date_obj.replace(year=date_obj.year + YEAR_ADDITION) + datetime.timedelta(days=DAY_ADDITION)
    return new_date_obj.strftime('%Y-%m-%d')

if __name__ == '__main__':
    sample_date = '2020-12-31'
    result_date = add_year_and_day(sample_date)
    print(result_date)