from datetime import date, timedelta

class DateCalculator:
    TARGET_WEEKDAY = 0

    @staticmethod
    def get_next_weekday(reference: date, target_weekday: int) -> date:
        current_weekday = reference.weekday()
        days_ahead = (target_weekday - current_weekday) % 7
        if days_ahead == 0:
            days_ahead = 7
        return reference + timedelta(days=days_ahead)

if __name__ == '__main__':
    calc = DateCalculator()
    start_date = date(2024, 2, 28)
    next_monday = calc.get_next_weekday(start_date, DateCalculator.TARGET_WEEKDAY)
    print(next_monday)