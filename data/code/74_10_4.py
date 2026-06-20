from datetime import datetime

class DayOfWeek:
    DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    @staticmethod
    def get_current_day():
        return DayOfWeek.DAYS[datetime.now().weekday()]

if __name__ == '__main__':
    print(DayOfWeek.get_current_day())