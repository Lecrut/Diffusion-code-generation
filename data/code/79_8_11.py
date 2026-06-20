import datetime

def get_next_month_date(date_obj):
    return date_obj.replace(day=1) + datetime.timedelta(days=32)

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 15)
    next_date = get_next_month_date(sample_date)
    print(f"Original Date: {sample_date}")
    print(f"Next Month's Date: {next_date}")
    
    sample_date_dec = datetime.date(2023, 12, 31)
    next_date_dec = get_next_month_date(sample_date_dec)
    print(f"Original Date: {sample_date_dec}")
    print(f"Next Month's Date: {next_date_dec}")