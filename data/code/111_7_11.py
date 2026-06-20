from datetime import datetime, timedelta

def add_year_and_day(date_str):
    date_format = "%Y-%m-%d"
    start_date = datetime.strptime(date_str, date_format)
    result_date = start_date + timedelta(days=365) + timedelta(days=1)
    return result_date.strftime(date_format)

if __name__ == '__main__':
    sample_date = "2020-12-31"
    print(add_year_and_day(sample_date))