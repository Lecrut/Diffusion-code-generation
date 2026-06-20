import datetime

def get_next_month(date_str):
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    if date_obj.month == 12:
        return datetime.date(date_obj.year + 1, 1, 1)
    else:
        return datetime.date(date_obj.year, date_obj.month + 1, 1)

if __name__ == '__main__':
    sample_date = "2023-12-15"
    next_date = get_next_month(sample_date)
    print(next_date.strftime("%Y-%m-%d"))