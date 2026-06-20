from datetime import date, timedelta

def next_monday(start_date):
    days_until_monday = (7 - start_date.weekday()) % 7
    return start_date + timedelta(days=days_until_monday)

if __name__ == '__main__':
    sample_date = date(2023, 9, 10)
    result = next_monday(sample_date)
    print(result)