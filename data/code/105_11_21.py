from datetime import date, timedelta

class MondayResolver:
    def __init__(self, anchor_date=None):
        self.anchor_date = anchor_date if anchor_date is not None else date.today()

    def resolve(self):
        current_weekday = self.anchor_date.weekday()
        days_ahead = (7 - current_weekday) % 7
        if days_ahead == 0:
            days_ahead = 7
        return self.anchor_date + timedelta(days=days_ahead)

if __name__ == '__main__':
    resolver = MondayResolver(date(2023, 10, 15))
    print(resolver.resolve().isoformat())