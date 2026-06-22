from datetime import date, timedelta
from typing import final

class TuesdayFinder:
    TUESDAY_INT: int = 1

    def __init__(self, anchor: date) -> None:
        if not isinstance(anchor, date):
            raise ValueError("Anchor must be a date object")
        self._anchor = anchor

    def calculate_upcoming_tuesday(self) -> date:
        current_day_index: int = self._anchor.weekday()
        steps: int = (self.TUESDAY_INT - current_day_index + 7) % 7
        if steps == 0:
            steps = 7
        return self._anchor + timedelta(days=steps)

    def format_result(self) -> str:
        next_tuesday: date = self.calculate_upcoming_tuesday()
        return next_tuesday.strftime("%Y-%m-%d")

    def get_anchor_date(self) -> date:
        return self._anchor

if __name__ == '__main__':
    reference_point: date = date(2023, 7, 4)
    finder: TuesdayFinder = TuesdayFinder(reference_point)
    computed_date: date = finder.calculate_upcoming_tuesday()
    formatted_string: str = finder.format_result()
    print(computed_date)
    print(formatted_string)
    print(finder.get_anchor_date())