import datetime
def get_next_month_date(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        next_month = date_obj.replace(month=date_obj.month + 1)
        if next_month.month > 12:
            next_month = next_month.replace(year=next_month.year + 1, month=1)
        return next_month.strftime("%Y-%m-%d")
    except ValueError:
        return "Error: Invalid date format. Please use YYYY-MM-DD."
if __name__ == '__main__':
    sample_date = "2023-10-15"
    result = get_next_month_date(sample_date)
    print(result)