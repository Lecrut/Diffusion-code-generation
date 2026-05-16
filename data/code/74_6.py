import datetime
def get_current_day_of_week(date_tuple):
    return date_tuple.weekday()
if __name__ == '__main__':
    sample_date_today = datetime.date.today()
    sample_date_monday = datetime.date(2023, 10, 23)
    sample_date_saturday = datetime.date(2023, 10, 28)
    result_today = get_current_day_of_week(sample_date_today)
    print(f"Today's day of the week index: {result_today}")
    assert 0 <= result_today <= 6
    print("Assertion passed for today's date.")
    result_monday = get_current_day_of_week(sample_date_monday)
    print(f"Monday's day of the week index: {result_monday}")
    assert result_monday == 0
    print("Assertion passed for Monday's date.")
    result_saturday = get_current_day_of_week(sample_date_saturday)
    print(f"Saturday's day of the week index: {result_saturday}")
    assert result_saturday == 5
    print("Assertion passed for Saturday's date.")