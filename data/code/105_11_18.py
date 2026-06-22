from datetime import date, timedelta

class MondayResolver:
    def __init__(self, anchor: date):
        self.anchor = anchor

    def resolve(self) -> date:
        current_weekday = self.anchor.weekday()
        days_to_add = (7 - current_weekday) % 7
        if days_to_add == 0:
            days_to_add = 7
        return self.anchor + timedelta(days=days_to_add)

if __name__ == '__main__':
    resolver = MondayResolver(date(2023, 10, 1))
    print(resolver.resolve().isoformat())