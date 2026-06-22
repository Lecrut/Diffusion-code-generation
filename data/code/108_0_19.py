import datetime

DAY_OF_MONTH_INDEX = 2

def extract_day_from_date(date_obj):
    if not isinstance(date_obj, datetime.date):
        raise ValueError("Input must be a datetime.date object")
    return date_obj.day

def format_day_output(day_value):
    return f"The day of the month is {day_value}"

if __name__ == '__main__':
    fixed_date = datetime.date(2025, 1, 1)
    day_value = extract_day_from_date(fixed_date)
    formatted_output = format_day_output(day_value)
    print(formatted_output)