from datetime import date, timedelta
from typing import Final

class DateResolver:
    TUESDAY_INDEX: Final[int] = 1
    _DAY_NAMES: Final[tuple[str, ...]] = (
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    )

    def __init__(self, anchor: date) -> None:
        self.anchor = anchor

    @staticmethod
    def _resolve_offset(current_weekday: int, target_weekday: int) -> int:
        diff = (target_weekday - current_weekday) % 7
        return 7 if diff == 0 else diff

    def get_next_tuesday(self) -> date:
        offset = self._resolve_offset(
            self.anchor.weekday(),
            DateResolver.TUESDAY_INDEX
        )
        return self.anchor + timedelta(days=offset)

    def get_tuesday_name(self) -> str:
        return self._DAY_NAMES[DateResolver.TUESDAY_INDEX]

if __name__ == '__main__':
    ref = date(2023, 7, 4)
    resolver = DateResolver(ref)
    next_tue = resolver.get_next_tuesday()
    print(next_tue)
    print(resolver.get_tuesday_name())