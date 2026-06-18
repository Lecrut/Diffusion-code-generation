import datetime as dt
def format_date_with_month(date_obj):
    return date_obj.strftime("%B")
if __name__ == '__main__':
    utc_time = dt.datetime.now(dt.timezone.utc)
    local_time = dt.datetime.now()
    print(format_date_with_month(utc_time))
    print(format_date_with_month(local_time))