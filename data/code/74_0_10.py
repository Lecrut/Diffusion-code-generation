import datetime

class DayOfWeekDetector:
    def __init__(self, reference_date=None):
        if reference_date is None:
            self.reference_date = datetime.date.today()
        else:
            self.reference_date = reference_date

    def get_name(self):
        return self.reference_date.strftime("%A")

    def get_short_name(self):
        return self.reference_date.strftime("%a")

    def get_index(self):
        return self.reference_date.weekday()

if __name__ == '__main__':
    detector = DayOfWeekDetector(datetime.date(2023, 10, 25))
    print(detector.get_name())
    print(detector.get_short_name())
    print(detector.get_index())