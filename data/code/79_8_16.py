import datetime

def get_next_month(date_str):
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    next_month = date_obj.replace(day=1) + datetime.timedelta(days=45)
    return next_month.replace(day=1)

if __name__ == '__main__':
    sample_date = "2023-10-15"
    next_month = get_next_month(sample_date)
    print(f"Original Date: {sample_date}")
    print(f"Next Month's First Day: {next_month.strftime('%Y-%m-%d')}")

    sample_date_dec = "2023-12-31"
    next_month_dec = get_next_month(sample_date_dec)
    print(f"Original Date: {sample_date_dec}")
    print(f"Next Month's First Day: {next_month_dec.strftime('%Y-%m-%d')}")