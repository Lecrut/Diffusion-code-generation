def extract_day_component(target_date):
    year = target_date.year
    month = target_date.month
    day = target_date.day
    return day

if __name__ == '__main__':
    import datetime
    reference_date = datetime.date(2023, 3, 15)
    day_value = extract_day_component(reference_date)
    print(day_value)