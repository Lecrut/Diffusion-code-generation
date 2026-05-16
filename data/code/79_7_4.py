import datetime
def get_next_month(date_obj):
    if date_obj.month == 12:
        next_month = 1
        next_year = date_obj.year + 1
    else:
        next_month = date_obj.month + 1
        next_year = date_obj.year
    return date_obj.replace(year=next_year, month=next_month)
if __name__ == '__main__':
    sample_date_str = "2023-12-15"
    sample_date = datetime.datetime.strptime(sample_date_str, "%Y-%m-%d").date()
    next_date = get_next_month(sample_date)
    print(next_date.strftime("%Y-%m-%d"))