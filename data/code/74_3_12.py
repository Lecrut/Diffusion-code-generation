from datetime import datetime

class DayOfWeek:
    @staticmethod
    def get_current_day():
        return datetime.now().strftime('%A')

if __name__ == '__main__':
    print(DayOfWeek.get_current_day())