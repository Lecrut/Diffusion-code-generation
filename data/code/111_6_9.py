from datetime import datetime, timedelta

def next_monday(start_date):
    delta = (7 - start_date.weekday()) % 7
    return start_date + timedelta(days=delta)

if __name__ == '__main__':
    sample_date = datetime(2023, 9, 10)
    result = next_monday(sample_date)
    print(result.strftime('%Y-%m-%d'))