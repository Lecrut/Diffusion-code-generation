from datetime import datetime, timedelta

WEEKDAY_MAP = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

TARGET_WEEKDAY_INDEX = 4

class DateCalculator:
    def __init__(self, reference_date: datetime):
        self.reference_date = reference_date

    def get_next_weekday(self, target_index: int) -> datetime:
        current_index = self.reference_date.weekday()
        days_offset = target_index - current_index
        if days_offset <= 0:
            days_offset += 7
        return self.reference_date + timedelta(days=days_offset)

if __name__ == '__main__':
    ref_date = datetime(2023, 12, 15)
    calculator = DateCalculator(ref_date)
    next_friday = calculator.get_next_weekday(TARGET_WEEKDAY_INDEX)
    print(next_friday.strftime("%Y-%m-%d"))