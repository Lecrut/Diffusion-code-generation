def get_day_of_month(date):
    return date.day

if __name__ == '__main__':
    from datetime import datetime
    sample_date = datetime(2023, 9, 15)
    print(get_day_of_month(sample_date))