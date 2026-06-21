import datetime

class DateAnalyzer:
    def __init__(self, date_string):
        self.date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()

    def get_day_name(self):
        return self.date_obj.strftime("%A")

    def get_iso_weekday(self):
        return self.date_obj.isoweekday()

    def get_full_date_string(self):
        return self.date_obj.isoformat()

if __name__ == '__main__':
    analyzer = DateAnalyzer("2023-10-05")
    print(analyzer.get_day_name())
    print(analyzer.get_iso_weekday())
    print(analyzer.get_full_date_string())