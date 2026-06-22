from datetime import datetime
from typing import Union

class DateExtractor:
    def __init__(self, date_input: Union[datetime, str]):
        if isinstance(date_input, str):
            self.dt = datetime.strptime(date_input, "%Y-%m-%d")
        elif isinstance(date_input, datetime):
            self.dt = date_input
        else:
            raise ValueError("Input must be a datetime object or a date string")

    def get_day(self) -> int:
        return self.dt.day

    def get_full_date(self) -> str:
        return self.dt.strftime("%Y-%m-%d")

if __name__ == '__main__':
    extractor = DateExtractor(datetime(2023, 10, 5))
    print(extractor.get_day())
    print(extractor.get_full_date())