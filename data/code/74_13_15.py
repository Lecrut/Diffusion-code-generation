from datetime import datetime

class DayOfWeekProvider:
    days = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }

    @staticmethod
    def get_current_day_of_week():
        return DayOfWeekProvider.days[datetime.now().weekday()]

if __name__ == '__main__':
    provider = DayOfWeekProvider()
    print(provider.get_current_day_of_week())