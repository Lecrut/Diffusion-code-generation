import calendar

class DateChecker:
    def is_weekday(self, date_obj):
        try:
            return date_obj.weekday() < 5
        except AttributeError:
            print('Invalid date object provided')
            return False

if __name__ == '__main__':
    checker = DateChecker()
    sample_date = datetime.date(2023, 10, 5)
    print(checker.is_weekday(sample_date))
    invalid_date = 'not a date'
    print(checker.is_weekday(invalid_date))