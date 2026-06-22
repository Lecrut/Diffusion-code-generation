from datetime import date

class DateEvaluator:
    def is_weekend(self, year, month, day):
        current_date = date(year, month, day)
        return current_date.weekday() >= 5

if __name__ == '__main__':
    evaluator = DateEvaluator()
    dates_to_check = [
        (2023, 10, 6),
        (2023, 10, 7),
        (2023, 10, 8)
    ]
    for year, month, day in dates_to_check:
        print(f"Is {year}-{month:02d}-{day:02d} a weekend? {evaluator.is_weekend(year, month, day)}")