import datetime
def get_current_day_of_week(date):
    return date.weekday()
if __name__ == '__main__':
    test_date_monday = datetime.date(2023, 10, 23)
    test_date_saturday = datetime.date(2023, 10, 28)
    test_date_sunday = datetime.date(2023, 10, 29)
    result_monday = get_current_day_of_week(test_date_monday)
    assert result_monday == 0
    print(f"Day of week for {test_date_monday}: {result_monday}")
    result_saturday = get_current_day_of_week(test_date_saturday)
    assert result_saturday == 5
    print(f"Day of week for {test_date_saturday}: {result_saturday}")
    result_sunday = get_current_day_of_week(test_date_sunday)
    assert result_sunday == 6
    print(f"Day of week for {test_date_sunday}: {result_sunday}")