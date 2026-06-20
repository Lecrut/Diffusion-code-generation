import datetime

class DayOfWeek:
    DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    @staticmethod
    def get_current_day():
        today = datetime.date.today()
        return DayOfWeek.DAYS[today.weekday()]

if __name__ == '__main__':
    current_day = DayOfWeek.get_current_day()
    print(current_day)