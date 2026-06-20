import datetime

class NextMondayFinder:
    def find_next_monday(self):
        today = datetime.date.today()
        days_until_monday = (7 - today.weekday()) % 7
        next_monday = today + datetime.timedelta(days=days_until_monday)
        return next_monday

if __name__ == '__main__':
    finder = NextMondayFinder()
    next_monday = finder.find_next_monday()
    print(next_monday)