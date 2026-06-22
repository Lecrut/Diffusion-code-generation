from datetime import date

def is_weekend(day):
    return day.weekday() >= 5

if __name__ == '__main__':
    sample_dates = [date(2023, 9, 16), date(2023, 9, 17), date(2023, 9, 18)]
    for day in sample_dates:
        print(f"{day}: {is_weekend(day)}")