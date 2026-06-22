import datetime

class DayOfWeekResolver:
    def __init__(self):
        self._date = datetime.date.today()

    def get_name(self):
        return self._date.strftime("%A")

    def get_abbreviation(self):
        return self._date.strftime("%a")

    def get_index(self):
        return self._date.weekday()

if __name__ == '__main__':
    resolver = DayOfWeekResolver()
    print(resolver.get_name())
    print(resolver.get_abbreviation())
    print(resolver.get_index())