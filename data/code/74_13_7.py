from datetime import datetime

class DayOfWeekService:
    def get_current_day_of_week(self):
        return datetime.now().strftime('%A')

if __name__ == '__main__':
    service = DayOfWeekService()
    print(service.get_current_day_of_week())