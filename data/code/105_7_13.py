from datetime import date, timedelta

class DateCalculator:
    REFERENCE_DATE = date(2023, 7, 4)

    @staticmethod
    def get_next_tuesday(start_date: date) -> date:
        days_until_tuesday = (1 + 6 - start_date.weekday()) % 7
        return start_date + timedelta(days=days_until_tuesday)

if __name__ == '__main__':
    upcoming_tuesday = DateCalculator.get_next_tuesday(DateCalculator.REFERENCE_DATE)
    print(upcoming_tuesday.strftime('%Y-%m-%d'))