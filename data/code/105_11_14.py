from datetime import date, timedelta

WEEK_START = 0

class DateResolver:
    def __init__(self, anchor: date = None):
        self.anchor = anchor if anchor is not None else date.today()

    def resolve_next_monday(self) -> date:
        current_weekday = self.anchor.weekday()
        days_to_add = (WEEK_START - current_weekday) % 7
        if days_to_add == 0:
            days_to_add = 7
        return self.anchor + timedelta(days=days_to_add)

if __name__ == '__main__':
    resolver = DateResolver(date(2024, 5, 20))
    result = resolver.resolve_next_monday()
    print(result.isoformat())