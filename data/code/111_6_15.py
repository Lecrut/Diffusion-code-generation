from datetime import date, timedelta

class DateUtils:
    @staticmethod
    def get_next_monday(start_date):
        days_to_add = (7 - start_date.weekday()) % 7
        return start_date + timedelta(days=days_to_add)

if __name__ == '__main__':
    sample_date = date(2023, 9, 10)
    next_monday = DateUtils.get_next_monday(sample_date)
    print(next_monday)