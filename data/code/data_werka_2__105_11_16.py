from datetime import date, timedelta

class MondayResolver:
    def __init__(self, start_date=None):
        self.start_date = start_date if start_date is not None else date.today()

    def resolve(self):
        current_weekday = self.start_date.weekday()
        days_to_add = (7 - current_weekday) % 7
        if days_to_add == 0:
            days_to_add = 7
        return self.start_date + timedelta(days=days_to_add)

if __name__ == '__main__':
    resolver = MondayResolver(date(2023, 10, 4))
    print(resolver.resolve().isoformat())