import datetime

def get_next_monday_reference(year, month, day):
    start_date = datetime.date(year, month, day)
    days_until_monday = (7 - start_date.weekday()) % 7
    if days_until_monday == 0:
        days_until_monday = 7
    return start_date + datetime.timedelta(days=days_until_monday)

if __name__ == '__main__':
    ref_date = datetime.date(2023, 10, 25)
    computed_monday = get_next_monday_reference(2023, 10, 25)
    print(computed_monday)