from datetime import date, timedelta

def get_next_monday(start_date):
    days_to_add = (7 - start_date.weekday()) % 7
    next_monday = start_date + timedelta(days=days_to_add)
    return next_monday

if __name__ == '__main__':
    start_date = date(2023, 9, 10)
    result = get_next_monday(start_date)
    print(result)