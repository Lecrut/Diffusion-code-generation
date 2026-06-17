import datetime
def format_and_validate_date(date_input):
    if not isinstance(date_input, (datetime.date, str)):
        raise TypeError("Input must be a date object or string.")
    try:
        parsed_date = None
        if isinstance(date_input, datetime.date):
            parsed_date = date_input
        elif isinstance(date_input, str):
            formatted_str = date_input.strip()
            try:
                if '-' in formatted_str and '/' not in formatted_str:
                    parsed_date = datetime.datetime.strptime(formatted_str, "%Y-%m-%d").date()
                elif ',' in formatted_str:
                    clean_str = formatted_str.replace("st", "").replace("nd", "").replace("rd", "").replace("th", "")
                    parsed_date = datetime.datetime.strptime(clean_str.split(",")[1], "%B %d, %Y").date()
                else:
                    raise ValueError(f"Unrecognized date format: {formatted_str}")
            except ValueError as e:
                raise ValueError(f"Invalid date string '{date_input}': {e}") from None
        if parsed_date is None or not isinstance(parsed_date, datetime.date):
            return "Date validation failed."
    except Exception as e:
        return f"Validation error occurred: {str(e)}"
    month_name = parsed_date.strftime("%B")
    formatted_str = f"{month_name} {parsed_date.day}, {parsed_date.year}"
    return formatted_str
if __name__ == '__main__':
    sample_dates = [
        datetime.date(2023, 10, 5),
        "October 4th, 2023",
        "2024-12-25"
    ]
    for date_val in sample_dates:
        result = format_and_validate_date(date_val)
        print(result)