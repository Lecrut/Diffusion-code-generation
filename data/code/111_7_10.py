from datetime import datetime, timedelta

def add_year_and_day(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    new_date = date + timedelta(days=365) + timedelta(days=1)
    return new_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    result = add_year_and_day('2020-12-31')
    print(result)