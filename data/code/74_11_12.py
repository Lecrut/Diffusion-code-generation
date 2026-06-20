import datetime

class DayOfWeekFinder:
    days_mapping = {
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
        return self.days_mapping[current_weekday]

if __name__ == '__main__':
    finder = DayOfWeekFinder()
    day_of_week = finder.get_current_day_of_week()
    print(day_of_week)