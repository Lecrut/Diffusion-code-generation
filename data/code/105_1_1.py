import datetime
def find_next_date(start_date_str):
    start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d')
    next_year = start_date.year + 1
    next_date = start_date.replace(year=next_year)
    return next_date.strftime('%Y-%m-%d')
if __name__ == '__main__':
    start_date1 = "2023-10-26"
    result1 = find_next_date(start_date1)
    print(f"Start Date: {start_date1}, Next Date: {result1}")
    start_date2 = "2024-01-01"
    result2 = find_next_date(start_date2)
    print(f"Start Date: {start_date2}, Next Date: {result2}")
    start_date3 = "1999-12-31"
    result3 = find_next_date(start_date3)
    print(f"Start Date: {start_date3}, Next Date: {result3}")