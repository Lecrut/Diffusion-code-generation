import datetime
def calculate_day_difference(start_date: str | datetime.datetime = None, end_date: str | datetime.datetime = None) -> int:
    def parse_date(date_input):
        if isinstance(date_input, datetime.datetime):
            return date_input.date()
        elif isinstance(date_input, str):
            try:
                dt = datetime.datetime.fromisoformat(date_input.replace('Z', '+00:00'))
                return dt.date()
            except ValueError:
                raise ValueError(f"Invalid date format for string input. Expected ISO 8601 or 'YYYY-MM-DD'.") from None
        else:
            raise TypeError("Date must be a datetime object, str, or int.")
    try:
        start = parse_date(start_date) if start_date is not None else datetime.date.today()
        end = parse_date(end_date) if end_date is not None else datetime.date.today()
        delta_days = (end - start).days
        return delta_days
    except ValueError as e:
        raise ValueError(f"Date parsing failed: {e}") from None
if __name__ == '__main__':
    result = calculate_day_difference(start_date="2023-01-01", end_date="2024-06-15")
    print(result)