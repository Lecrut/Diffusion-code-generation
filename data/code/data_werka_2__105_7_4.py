from datetime import date, timedelta
from typing import ClassVar

WEEKDAY_TUESDAY: int = 1

class DateNavigator:
    _TUESDAY_INDEX: ClassVar[int] = 1

    def __init__(self, anchor: date) -> None:
        self.anchor = anchor

    def _compute_offset(self, target_day: int) -> int:
        current_idx: int = self.anchor.weekday()
        raw_diff: int = (target_day - current_idx) % 7
        return 7 if raw_diff == 0 else raw_diff

    def get_upcoming_tuesday(self) -> date:
        days_to_add: int = self._compute_offset(self._TUESDAY_INDEX)
        return self.anchor + timedelta(days=days_to_add)

    def get_weekday_name(self) -> str:
        days: list[str] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[self.anchor.weekday()]

if __name__ == '__main__':
    start: date = date(2023, 7, 4)
    nav: DateNavigator = DateNavigator(start)
    tuesday_date: date = nav.get_upcoming_tuesday()
    current_name: str = nav.get_weekday_name()
    print(tuesday_date)
    print(current_name)