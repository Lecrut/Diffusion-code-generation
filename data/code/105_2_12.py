from datetime import date, timedelta

class DateHelper:
    TARGET_DAY = 5

    @staticmethod
    def calculate_next_friday(reference_date):
        days_until_target = (DateHelper.TARGET_DAY - reference_date.weekday()) % 7
        if days_until_target == 0:
            days_until_target = 7
        return reference_date + timedelta(days=days_until_target)
if __name__ == '__main__':
    sample_date = date(2023, 12, 15)
    next_friday = DateHelper.calculate_next_friday(sample_date)
    print(next_friday.strftime('%Y-%m-%d'))