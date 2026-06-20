def get_day_of_month(date_obj):
    return date_obj.day

if __name__ == '__main__':
    from datetime import date
    sample_date = date(2023, 9, 15)
    print(get_day_of_month(sample_date))