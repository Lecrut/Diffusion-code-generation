import datetime

class DateUtility:
    def __init__(self, year, month, day):
        self.date_obj = datetime.date(year, month, day)

    def get_weekday_upper(self):
        return self.date_obj.strftime('%A').upper()

    def get_iso_weekday(self):
        return self.date_obj.isoweekday()

if __name__ == '__main__':
    analyzer = DateUtility(2024, 7, 4)
    print(analyzer.get_weekday_upper())
    print(analyzer.get_iso_weekday())