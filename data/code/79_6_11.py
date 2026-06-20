from datetime import date, timedelta

def next_month(date_obj):
    if date_obj.month == 12:
        return date_obj.replace(year=date_obj.year + 1, month=1)
    else:
        return date_obj.replace(month=date_obj.month + 1)

if __name__ == '__main__':
    sample_date = date(2023, 10, 15)
    print(next_month(sample_date))