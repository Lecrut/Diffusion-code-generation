import datetime
from dateutil import parser as date_parser_lib                                
def calculate_days_between(ts1_str: str, ts2_str: str) -> int:
    if not (ts1_str and ts2_str):
        raise ValueError("Both timestamp strings must be provided.")
    try:
        dt1 = date_parser_lib.parse(ts1_str)
        dt2 = date_parser_lib.parse(ts2_str)
    except Exception as e:
        raise ValueError(f"Invalid date format in input. Error details: {str(e)}") from None
    if not isinstance(dt1, datetime.datetime):
        try:
            dt1 = datetime.datetime.fromtimestamp(float(str(dt1)))
        except (ValueError, TypeError) as e:
            raise ValueError("Failed to convert parsed date object.") from e
    if not isinstance(dt2, datetime.datetime):
        try:
            dt2 = datetime.datetime.fromtimestamp(float(str(dt2)))
        except (ValueError, TypeError) as e:
            raise ValueError("Failed to convert parsed date object.") from e
    delta = abs((dt1 - dt2).days)
    return int(delta)
if __name__ == '__main__':
    sample_input_1 = "January 5th, 2023"
    sample_input_2 = "March 14th, 2023"
    result_days = calculate_days_between(sample_input_1, sample_input_2)
    print(f"Days between {sample_input_1} and {sample_input_2}: {result_days}")