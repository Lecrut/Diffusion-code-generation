from datetime import date
def format_and_validate_date(date_input: str) -> str:
    try:
        parsed_date = date.fromisoformat(date_input.replace("-", " "))
    except ValueError as e:
        raise ValueError(f"Invalid date format provided: {date_input}") from e
    if not isinstance(parsed_date, date):
        raise TypeError("Input must be a valid ISO 8601 formatted string representing a calendar date.")
    month_name = parsed_date.strftime("%B")
    return f"{month_name} {parsed_date.day}"
if __name__ == '__main__':
    sample_input_1 = "2023-05-17"
    sample_input_2 = "invalid-date-string"
    try:
        result_1 = format_and_validate_date(sample_input_1)
        print(f"{sample_input_1} -> {result_1}")
    except ValueError as ve:
        print(f"Error processing {sample_input_1}: {ve}")
    try:
        result_invalid = format_and_validate_date(sample_input_2)
        print(result_invalid)
    except (ValueError, TypeError):
        pass