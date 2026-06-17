import datetime as dt
def format_date_with_month_name(date_obj):
    return date_obj.strftime("%B %d, %Y")
if __name__ == '__main__':
    sample_dates = [dt.date(2023, 5, 17), dt.datetime.now(), "2024-08-30"]
    for d in sample_dates:
        if isinstance(d, str):
            parsed_date = dt.datetime.strptime(d, "%Y-%m-%d").date()
        else:
            parsed_date = d
        result = format_date_with_month_name(parsed_date)
        print(result)