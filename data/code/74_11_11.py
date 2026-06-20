import datetime

class DayOfWeekFinder:
    def __init__(self):
        self.days_mapping = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"
        }
    
    def validate_weekday(self, weekday):
        if not isinstance(weekday, int) or weekday < 0 or weekday > 6:
            raise ValueError("Weekday must be an integer between 0 and 6")
    
    def get_current_day_of_week(self):
        current_weekday = datetime.datetime.now().weekday()
        self.validate_weekday(current_weekday)
        return self.days_mapping[current_weekday]

if __name__ == '__main__':
    finder = DayOfWeekFinder()
    print(finder.get_current_day_of_week())