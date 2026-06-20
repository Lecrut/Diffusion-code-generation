from datetime import datetime

class DateWeekChecker:
    DATE_FORMAT = '%Y-%m-%d'

    @staticmethod
    def is_same_week(date_str1: str, date_str2: str) -> bool:
        date1 = datetime.strptime(date_str1, DateWeekChecker.DATE_FORMAT)
        date2 = datetime.strptime(date_str2, DateWeekChecker.DATE_FORMAT)
        return date1.isocalendar()[1] == date2.isocalendar()[1]

if __name__ == '__main__':
    checker = DateWeekChecker()
    print(checker.is_same_week('2023-10-01', '2023-10-07'))
    print(checker.is_same_week('2023-10-01', '2023-10-08'))