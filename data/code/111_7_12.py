from datetime import datetime, timedelta

def add_year_and_day(date_str):
    date_format = "%Y-%m-%d"
    date_obj = datetime.strptime(date_str, date_format)
    new_date_obj = date_obj + timedelta(days=365) + timedelta(days=1)
    return new_date_obj.strftime(date_format)

if __name__ == '__main__':
    result = add_year_and_day("2020-12-31")
    print(result)