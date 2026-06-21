def get_day_of_month(date_obj):
    return date_obj.day

if __name__ == '__main__':
    import datetime
    sample_date = datetime.date(2023, 3, 15)
    result = get_day_of_month(sample_date)
    print(result)