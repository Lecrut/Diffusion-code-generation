import datetime

class DayOfWeekFinder:
    DAYS_OF_WEEK = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }

    def get_current_day_of_week(self):
        current_weekday = datetime.datetime.now().weekday()
        return self.DAYS_OF_WEEK[current_weekday]

if __name__ == '__main__':
    finder = DayOfWeekFinder()
    print(finder.get_current_day_of_week())