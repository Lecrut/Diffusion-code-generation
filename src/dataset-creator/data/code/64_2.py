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
            for fmt in ["%Y-%m-%d", "%B %d, %Y", "%d/%m/%Y"]:
                try:
                    parsed_date = datetime.datetime.strptime(formatted_str, fmt).date()
                    break
                except ValueError:
                    continue
            if not isinstance(parsed_date, datetime.date):
                raise ValueError(f"Unable to parse date string '{formatted_str}'")
        return parsed_date.strftime("%B %d, %Y")
    except Exception as e:
        raise RuntimeError(f"Date processing failed due to {str(e)}")
if __name__ == '__main__':
    sample_dates = [
        datetime.date(2023, 10, 5),
        "October 5, 2023",
        "05/10/2023"
    ]
    for date in sample_dates:
        try:
            result = format_and_validate_date(date)
            print(f"{date} -> {result}")
        except Exception as e:
            print(f"Error processing {date}: {e}")