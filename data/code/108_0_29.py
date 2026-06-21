import datetime

def extract_day_component(date_instance):
    if not isinstance(date_instance, datetime.date):
        raise ValueError("Expected a datetime.date object")
    return date_instance.day

if __name__ == '__main__':
    target = datetime.date(2025, 1, 1)
    day_value = extract_day_component(target)
    print(day_value)