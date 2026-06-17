import datetime
from typing import List, Union
def format_date(date_input: Union[str, datetime.date]) -> str:
    if isinstance(date_input, str):
        try:
            parsed = datetime.datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
            return "Invalid date format"
    elif hasattr(date_input, 'strftime'):
        parsed = date_input
    else:
        raise TypeError("Input must be a string or date-like object")
    month_name = parsed.strftime("%B %d, %Y")
    return f"{parsed.year}-{month_name}"
def process_large_dataset(input_data: List[str]) -> List[str]:
    try:
        return [format_date(date) for date in input_data]
    except Exception as e:
        print(f"Error processing dataset: {e}")
        return []
if __name__ == '__main__':
    sample_dates = ["2023-10-05", "2024-01-15", "2025-06-20"]
    results = process_large_dataset(sample_dates)
    for result in results:
        print(result)