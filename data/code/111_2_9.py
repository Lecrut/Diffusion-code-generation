import datetime

def get_day_of_week(year, month, day):
    try:
        date = datetime.date(year, month, day)
        return date.strftime('%A')
    except ValueError as e:
        raise ValueError(f"Invalid date: {e}")

if __name__ == '__main__':
    sample_year = 2024
    sample_month = 2
    sample_day = 29
    print(f"Day of the week for February 29, 2024: {get_day_of_week(sample_year, sample_month, sample_day)}")