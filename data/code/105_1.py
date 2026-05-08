import datetime
def find_next_date(start_date_str):
    start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d')
    next_year = start_date.year + 1
    next_date = start_date.replace(year=next_year)
    return next_date.strftime('%Y-%m-%d')
if __name__ == '__main__':
    start_date = "2023-10-26"
    next_date = find_next_date(start_date)
    print(next_date)