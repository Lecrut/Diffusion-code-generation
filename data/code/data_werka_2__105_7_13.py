from datetime import date, timedelta
from typing import ClassVar

class TuesdayFinder:
    _TARGET_WEEKDAY: ClassVar[int] = 1
    _OFFSET_MULTIPLIER: ClassVar[int] = 7

    def __init__(self, anchor: date) -> None:
        if not isinstance(anchor, date):
            raise ValueError("Anchor must be a date instance")
        self.anchor = anchor

    @staticmethod
    def _calculate_days_offset(current_weekday: int, target_weekday: int) -> int:
        raw_offset = (target_weekday - current_weekday) % TuesdayFinder._OFFSET_MULTIPLIER
        return TuesdayFinder._OFFSET_MULTIPLIER if raw_offset == 0 else raw_offset

    def find_next_tuesday(self) -> date:
        current_weekday = self.anchor.weekday()
        days_to_add = self._calculate_days_offset(current_weekday, self._TARGET_WEEKDAY)
        return self.anchor + timedelta(days=days_to_add)

if __name__ == '__main__':
    reference = date(2023, 7, 4)
    finder = TuesdayFinder(reference)
    result = finder.find_next_tuesday()
    print(result)