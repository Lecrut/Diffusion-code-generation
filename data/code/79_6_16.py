from datetime import date, timedelta

class DateManipulator:
    MONTHS_IN_YEAR = 12

    @staticmethod
    def get_next_month(target_date):
        next_month = target_date.month % DateManipulator.MONTHS_IN_YEAR + 1
        next_year = target_date.year + (target_date.month == DateManipulator.MONTHS_IN_YEAR)
        return date(next_year, next_month)

if __name__ == '__main__':
    sample_date = date(2023, 10, 15)
    print(DateManipulator.get_next_month(sample_date))