from datetime import date

def _validate_date_input(value):
    if not isinstance(value, date):
        raise ValueError("Argument must be a datetime.date instance")
    return value

def get_date_diff_in_days(first_date, second_date):
    validated_first = _validate_date_input(first_date)
    validated_second = _validate_date_input(second_date)
    delta = validated_second - validated_first
    return delta.days

if __name__ == '__main__':
    start = date(2020, 2, 28)
    end = date(2020, 3, 1)
    diff = get_date_diff_in_days(start, end)
    print(diff)