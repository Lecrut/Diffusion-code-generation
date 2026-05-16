import datetime
def get_next_month(date_string):
    date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
    year = date_obj.year
    month = date_obj.month
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    return datetime.date(next_year, next_month, date_obj.day)
if __name__ == '__main__':
    sample_date = "2023-12-15"
    next_date = get_next_month(sample_date)
    print(next_date.strftime("%Y-%m-%d"))