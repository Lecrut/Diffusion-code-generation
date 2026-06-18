import datetime
def format_date(date_obj: datetime.date) -> str:
    return date_obj.strftime("%B %d, %Y")
class BatchProcessorError(Exception):
    pass
def process_batch(dates_list: list) -> list[str]:
    if not isinstance(dates_list, list):
        raise BatchProcessorError("Input must be a list.")
    formatted_dates = []
    for idx, date_input in enumerate(dates_list):
        try:
            parsed_date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
            if not isinstance(parsed_date, datetime.date):
                raise BatchProcessorError(f"Invalid date format at index {idx}.")
            formatted_str = format_date(parsed_date)
            formatted_dates.append(formatted_str)
        except ValueError as e:
            raise BatchProcessorError(f"Date parsing error at index {idx}: {e}") from None
    return formatted_dates
if __name__ == '__main__':
    sample_inputs = [
        "2023-10-05",
        "2024-01-15",
        "invalid-date"
    ]
    try:
        result = process_batch(sample_inputs)
        print(result)
    except BatchProcessorError as e:
        print(f"Processing failed: {e}")