import datetime
from typing import List
def format_date(date_obj: datetime.date) -> str:
    return date_obj.strftime("%B %d, %Y")
if __name__ == '__main__':
    sample_dates = [
        datetime.datetime(2023, 1, 5),
        datetime.datetime(2024, 6, 15),
        datetime.datetime(2025, 12, 31)
    ]
    formatted_output: List[str] = []
    for date in sample_dates:
        try:
            formated_date_str = format_date(date.date())
            formatted_output.append(formated_date_str)
        except Exception as e:
            print(f"Error processing {date}: {e}")
    result_string = "\n".join(formatted_output)
    print(result_string)