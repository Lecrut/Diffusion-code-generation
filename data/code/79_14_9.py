import datetime

def get_next_month_date(date_obj):
    year = date_obj.year + (date_obj.month // 12)
    month = (date_obj.month % 12) + 1
    return datetime.date(year, month, 1)

if __name__ == '__main__':
    sample_date = datetime.date(2024, 3, 31)
    result = get_next_month_date(sample_date)
    print(result.strftime('%Y-%m-%d'))