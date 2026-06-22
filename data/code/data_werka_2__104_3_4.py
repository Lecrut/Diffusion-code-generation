from datetime import date

def validate_date_input(obj):
    if not isinstance(obj, date):
        raise ValueError("Expected a date instance")
    return obj

def compute_date_span(first: date, second: date) -> int:
    validated_first = validate_date_input(first)
    validated_second = validate_date_input(second)
    span = validated_second - validated_first
    return span.days

if __name__ == '__main__':
    start = date(2024, 1, 1)
    end = date(2024, 1, 15)
    total_days = compute_date_span(start, end)
    print(total_days)