import datetime

class DayOfWeek:
    def __init__(self):
        self.current_day = datetime.datetime.now().weekday()

    def get_day_name(self):
        days = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"
        }
        return days[self.current_day]

if __name__ == '__main__':
    day_of_week = DayOfWeek()
    print(day_of_week.get_day_name())