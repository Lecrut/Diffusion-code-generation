import datetime
if __name__ == '__main__':
    sample_date_str = "2023-10-15"
    sample_date = datetime.datetime.strptime(sample_date_str, "%Y-%m-%d").date()
    next_month = sample_date.replace(day=1) + datetime.timedelta(days=32)
    next_month = next_month.replace(day=1)
    print(next_month.strftime("%B %d, %Y"))