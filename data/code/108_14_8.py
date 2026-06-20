def get_day_of_month(date):
    return date.day

if __name__ == '__main__':
    from datetime import date
    sample_date = date(2023, 4, 15)
    print(get_day_of_month(sample_date))