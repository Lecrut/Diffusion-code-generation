from datetime import date

class DateAnalyzer:
    def __init__(self, iso_date):
        self.date_obj = date.fromisoformat(iso_date)

    def get_day_of_week(self):
        day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return day_names[self.date_obj.weekday()]

    def is_weekday(self):
        return self.date_obj.weekday() < 5

if __name__ == '__main__':
    analyzer1 = DateAnalyzer("2023-10-25")
    print(f"Date: {analyzer1.date_obj}, Day of the week: {analyzer1.get_day_of_week()}, Is weekday: {analyzer1.is_weekday()}")
    
    analyzer2 = DateAnalyzer("2023-10-28")
    print(f"Date: {analyzer2.date_obj}, Day of the week: {analyzer2.get_day_of_week()}, Is weekday: {analyzer2.is_weekday()}")
    
    analyzer3 = DateAnalyzer("2023-10-29")
    print(f"Date: {analyzer3.date_obj}, Day of the week: {analyzer3.get_day_of_week()}, Is weekday: {analyzer3.is_weekday()}")