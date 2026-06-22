import datetime

def calculate_next_monday(target_date: datetime.date) -> datetime.date:
    days_until_monday = (0 - target_date.weekday()) % 7
    if days_until_monday == 0:
        days_until_monday = 7
    return target_date + datetime.timedelta(days=days_until_monday)

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 15)
    result = calculate_next_monday(sample_date)
    print(result)