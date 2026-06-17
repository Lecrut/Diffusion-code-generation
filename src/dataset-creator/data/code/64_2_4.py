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
            for fmt in ["%B %d, %Y", "%b %d, %Y", "%Y-%m-%d"]:
                try:
                    parsed_date = datetime.datetime.strptime(formatted_str, fmt).date()
                    break
                except ValueError:
                    continue
            if not isinstance(parsed_date, datetime.date):
                raise ValueError(f"Unable to parse date string '{formatted_str}'")
        return {
            "original": str(date_input),
            "parsed": parsed_date.isoformat(),
            "localized_string": parsed_date.strftime("%B %d, %Y"),
            "day_of_week": parsed_date.strftime("%A"),
            "year_month_day": f"{parsed_date.year}-{int(parsed_date.month):02d}-{int(parsed_date.day):02d}"
        }
    except Exception as e:
        raise ValueError(f"Date processing failed due to error: {str(e)}")
if __name__ == '__main__':
    sample_dates = [
        datetime.date(2023, 10, 5),
        "October 5, 2023",
        "Oct 5, 2023",
        "2024-07-15"
    ]
    for date_val in sample_dates:
        try:
            result = format_and_validate_date(date_val)
            print(f"Input: {result['original']}")
            print(f"Parsed ISO Format: {result['parsed']}")
            print(f"Localized String (English): {result['localized_string']}")
            print(f"Day of Week: {result['day_of_week']}")
            print(f"Year-Month-Day: {result['year_month_day']}")
        except Exception as e:
            print(f"Error processing input '{date_val}': {e}")