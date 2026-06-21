import calendar
from datetime import datetime

class DayClassifier:
    def __init__(self, date_value: datetime):
        if not isinstance(date_value, datetime):
            raise ValueError("Input must be a datetime object")
        self.date_value = date_value

    def is_weekday(self) -> bool:
        day_index = calendar.weekday(self.date_value.year, self.date_value.month, self.date_value.day)
        return day_index in (0, 1, 2, 3, 4)

    def get_weekday_index(self) -> int:
        return calendar.weekday(self.date_value.year, self.date_value.month, self.date_value.day)

if __name__ == '__main__':
    target_date = datetime(2023, 10, 23)
    classifier = DayClassifier(target_date)
    print(classifier.is_weekday())
    print(classifier.get_weekday_index())