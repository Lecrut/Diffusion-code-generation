import datetime

class DayOfWeekFinder:
    DAY_MAPPING = {
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
        now = datetime.datetime.now()
        current_weekday = now.weekday()
        return DayOfWeekFinder.DAY_MAPPING[current_weekday]

if __name__ == '__main__':
    finder = DayOfWeekFinder()
    print(finder.get_current_day_of_week())