import datetime

class DateAnalyzer:
    def __init__(self, date_obj=None):
        if date_obj is None:
            self.date_obj = datetime.date.today()
        else:
            self.date_obj = date_obj

    def get_day_name(self):
        return self.date_obj.strftime('%A')

    def get_day_number(self):
        return self.date_obj.weekday()

    def get_iso_weekday(self):
        return self.date_obj.isoweekday()

if __name__ == '__main__':
    analyzer = DateAnalyzer()
    print(analyzer.get_day_name())
    print(analyzer.get_day_number())
    print(analyzer.get_iso_weekday())