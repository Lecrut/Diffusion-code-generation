from datetime import datetime

class DayOfWeek:
    def __init__(self):
        self.days = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"
        }

    def get_current_day_of_week(self):
        return self.days[datetime.now().weekday()]

if __name__ == '__main__':
    day_formatter = DayOfWeek()
    print(day_formatter.get_current_day_of_week())