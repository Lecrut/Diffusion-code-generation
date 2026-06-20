import datetime

class DayOfWeekFinder:
    def get_today(self):
        return datetime.datetime.now().strftime('%A')

if __name__ == '__main__':
    finder = DayOfWeekFinder()
    print(finder.get_today())