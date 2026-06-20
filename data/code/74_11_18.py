import datetime

class DayOfWeekFinder:
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    def get_current_day_of_week(self):
        today = datetime.datetime.now()
        return self.day_names[today.weekday()]

if __name__ == '__main__':
    finder = DayOfWeekFinder()
    sample_day = finder.get_current_day_of_week()
    print(f"Today is: {sample_day}")