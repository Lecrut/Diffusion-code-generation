from datetime import date, timedelta

class MondayScheduler:
    def __init__(self, anchor: date = None):
        self.anchor = anchor if anchor is not None else date.today()

    def resolve_next_monday(self) -> date:
        current_index = self.anchor.weekday()
        steps = (7 - current_index) % 7
        if steps == 0:
            steps = 7
        return self.anchor + timedelta(days=steps)

if __name__ == '__main__':
    scheduler = MondayScheduler(date(2024, 5, 20))
    target = scheduler.resolve_next_monday()
    print(target.isoformat())