import datetime
def format_date(date_obj: datetime.date) -> str:
    return date_obj.strftime("%B %d, %Y")
class BatchProcessorError(Exception):
    pass
def process_dates(dates_list: list) -> dict[str, str]:
    result = {}
    for idx, input_val in enumerate(dates_list):
        try:
            if isinstance(input_val, datetime.date):
                formatted_date = format_date(input_val)
                result[idx] = formatted_date
            elif isinstance(input_val, (int, float)):
                date_obj = datetime.datetime.fromtimestamp(input_val).date()
                formatted_date = format_date(date_obj)
                result[int(idx)] = formatted_date
            else:
                raise BatchProcessorError(f"Unsupported input type at index {idx}: {type(input_val)}")
        except Exception as e:
            error_msg = f"Processing failed for value '{input_val}': {str(e)}"
            if idx in result:
                del result[idx]
            else:
                raise BatchProcessorError(error_msg) from None
    return result
if __name__ == '__main__':
    sample_inputs = [datetime.date(2023, 10, 5), "1697488800", datetime.datetime.strptime("2023-07-20", "%Y-%m-%d").date()]
    try:
        output_data = process_dates(sample_inputs)
        for key, value in output_data.items():
            print(f"Index {key}: {value}")
    except BatchProcessorError as e:
        print(f"Critical Error: {e}", file=__import__('sys').stderr)