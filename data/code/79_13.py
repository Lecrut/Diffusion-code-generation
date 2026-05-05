import datetime
if __name__ == '__main__':
    date_str = "2023-10-15"
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    next_month = date_obj.replace(day=1) + datetime.timedelta(days=32)
    next_month_date = next_month.replace(day=1)
    print(next_month_date.strftime("%Y-%m-%d"))