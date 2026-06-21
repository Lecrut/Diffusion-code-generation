from datetime import date, timedelta
from typing import Optional

class MondayResolver:
    def __init__(self, anchor: Optional[date] = None):
        self.anchor = anchor if anchor is not None else date.today()
    def resolve(self) -> date:
        weekday = self.anchor.weekday()
        offset = 7 if weekday == 0 else (7 - weekday)
        return self.anchor + timedelta(days=offset)
if __name__ == '__main__':
    resolver = MondayResolver(date(2024, 5, 20))
    result = resolver.resolve()
    print(result.isoformat())