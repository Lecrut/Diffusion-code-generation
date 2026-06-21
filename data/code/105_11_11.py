from datetime import date, timedelta

class MondayResolver:
    def __init__(self, base_date=None):
        self.base_date = base_date if base_date is not None else date.today()

    def resolve(self):
        current_weekday = self.base_date.weekday()
        days_offset = (7 - current_weekday) % 7
        if days_offset == 0:
            days_offset = 7
        return self.base_date + timedelta(days=days_offset)

if __name__ == '__main__':
    resolver = MondayResolver(date(2024, 5, 20))
    print(resolver.resolve().isoformat())