import datetime

class DateWeekDifference:
    def __init__(self, date_str1, date_str2):
        self.date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d').date()
        self.date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d').date()

    def calculate_week_difference(self):
        difference = abs(self.date2 - self.date1)
        weeks = difference.days // 7
        return weeks

if __name__ == '__main__':
    instance1 = DateWeekDifference("2023-01-01", "2023-01-08")
    print(instance1.calculate_week_difference())
    
    instance2 = DateWeekDifference("2023-01-01", "2023-01-07")
    print(instance2.calculate_week_difference())
    
    instance3 = DateWeekDifference("2023-01-01", "2023-01-01")
    print(instance3.calculate_week_difference())