import datetime

def is_weekday(d: datetime.date) -> bool:
    day_index = d.weekday()
    is_monday = day_index == 0
    is_friday = day_index == 4
    return is_monday or is_friday

if __name__ == '__main__':
    test_date = datetime.date(2024, 12, 25)
    output = is_weekday(test_date)
    print(output)