from datetime import date, timedelta

class NextMondayFinder:
    def __init__(self, reference_date=None):
        self.reference_date = reference_date if reference_date is not None else date.today()

    def get_next_monday(self):
        days_until_monday = (7 - self.reference_date.weekday()) % 7
        if days_until_monday == 0:
            days_until_monday = 7
        return self.reference_date + timedelta(days=days_until_monday)

if __name__ == '__main__':
    finder = NextMondayFinder(date(2023, 10, 1))
    result = finder.get_next_monday()
    print(result.isoformat())