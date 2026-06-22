from datetime import datetime
from typing import List

class DateValidator:
    def __init__(self, date_string: str) -> None:
        self.date_string = date_string
        self.parsed_date = datetime.fromisoformat(date_string)

    def is_weekday(self) -> bool:
        return self.parsed_date.weekday() < 5

    def get_day_name(self) -> str:
        return self.parsed_date.strftime("%A")

if __name__ == '__main__':
    validator1 = DateValidator("2023-10-06")
    validator2 = DateValidator("2023-10-07")
    
    print(validator1.is_weekday())
    print(validator2.is_weekday())
    print(validator1.get_day_name())
    print(validator2.get_day_name())