import datetime

class DateAnalyzer:
    def __init__(self, iso_string):
        self.date_obj = datetime.date.fromisoformat(iso_string)

    def get_weekday_index(self):
        return self.date_obj.weekday()

    def get_weekday_name(self):
        names = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        return names[self.date_obj.weekday()]

    def is_weekend(self):
        idx = self.date_obj.weekday()
        return idx >= 5

if __name__ == '__main__':
    analyzer = DateAnalyzer('2024-07-04')
    print(analyzer.get_weekday_index())
    print(analyzer.get_weekday_name())
    print(analyzer.is_weekend())