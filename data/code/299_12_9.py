from datetime import date

def is_weekend(date_list):
    weekend_dates = [date(2023, 10, 7), date(2023, 10, 8)]
    return any((d in weekend_dates for d in date_list))
if __name__ == '__main__':
    sample_dates = [date(2023, 10, 6), date(2023, 10, 7)]
    print(is_weekend(sample_dates))