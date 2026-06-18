import datetime
def format_date(date_obj: datetime.date) -> str:
    return date_obj.strftime("%B %d, %Y")
class BatchProcessorError(Exception):
    pass
def process_batch(input_dates: list) -> dict[str, bool]:
    results = {}
    for idx, input_str in enumerate(input_dates):
        try:
            parsed_date = datetime.datetime.strptime(input_str, "%m/%d/%Y").date()
            formatted_output = format_date(parsed_date)
            results[input_str] = True
        except ValueError as e:
            error_msg = f"Invalid date format at index {idx}: {input_str}. Error details: {e}"
            raise BatchProcessorError(error_msg) from e
    return results
if __name__ == '__main__':
    sample_inputs = ["01/15/2023", "invalid_date", "06/30/2024"]
    try:
        output_map = process_batch(sample_inputs)
        for input_val, success in output_map.items():
            print(f"Input: {input_val} -> {'Success' if success else 'Error'}")
    except BatchProcessorError as e:
        print(e)