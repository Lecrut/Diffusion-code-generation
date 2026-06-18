import datetime
from typing import List
def format_date(date_obj: datetime.date) -> str:
    return date_obj.strftime("%B %d, %Y")
if __name__ == '__main__':
    sample_dates = [
        datetime.datetime(2023, 5, 17),
        datetime.datetime(2024, 1, 1),
        datetime.datetime(2022, 12, 31)
    ]
    formatted_output: List[str] = []
    for date in sample_dates:
        try:
            formated_date_str = format_date(date.date())
            formatted_output.append(formated_date_str)
        except Exception as e:
            print(f"Error processing {date}: {e}")
    result_string = "\n".join(formatted_output)
    with open("formatted_dates.txt", "w") as f:
        f.write(result_string)