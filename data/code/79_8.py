import datetime
def get_next_month(date_str):
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    if date_obj.month == 12:
        next_month = date_obj.replace(year=date_obj.year + 1, month=1, day=1)
    else:
        next_month = date_obj.replace(month=date_obj.month + 1, day=date_obj.day)
    return next_month.strftime("%Y-%m-%d")
if __name__ == '__main__':
    sample_date = "2023-10-15"
    next_date = get_next_month(sample_date)
    print(f"Original Date: {sample_date}")
    print(f"Next Month's Date: {next_date}")
    sample_date_dec = "2023-12-31"
    next_date_dec = get_next_month(sample_date_dec)
    print(f"Original Date: {sample_date_dec}")
    print(f"Next Month's Date: {next_date_dec}")