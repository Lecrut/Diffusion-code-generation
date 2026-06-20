from datetime import date, timedelta

def get_next_monday(start_date):
    days_until_monday = (7 - start_date.weekday()) % 7
    return start_date + timedelta(days=days_until_monday)

if __name__ == '__main__':
    sample_date = date(2023, 9, 10)
    next_monday = get_next_monday(sample_date)
    print(next_monday)