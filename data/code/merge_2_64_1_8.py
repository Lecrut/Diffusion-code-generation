import datetime
from typing import Union
def normalize_date(date_input: Union[str, datetime.datetime]) -> str:
    if isinstance(date_input, datetime.datetime):
        return date_input.strftime("%B %d, %Y")
    try:
        parsed = datetime.datetime.strptime(date_input, "%m/%d/%Y")
        return parsed.strftime("%B %d, %Y")
    except ValueError:
        raise ValueError(f"Unable to parse date string '{date_input}' into a recognized format.")
if __name__ == '__main__':
    sample_dates = [
        "12/25/2023",
        datetime.datetime(2024, 6, 15),
        "08/01/2020"
    ]
    for date in sample_dates:
        print(normalize_date(date))