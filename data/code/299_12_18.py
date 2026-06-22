from datetime import date

def is_weekend(date_list):
    weekend_dates = []
    for d in date_list:
        if d.weekday() >= 5:
            weekend_dates.append(d)
    return weekend_dates
if __name__ == '__main__':
    sample_dates = [date(2023, 10, 7), date(2023, 10, 8), date(2023, 10, 9)]
    result = is_weekend(sample_dates)
    print(result)