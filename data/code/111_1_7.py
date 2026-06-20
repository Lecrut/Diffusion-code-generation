import datetime

class DateManipulator:
    def add_30_days(self, date_obj):
        return date_obj + datetime.timedelta(days=30)

if __name__ == '__main__':
    manipulator = DateManipulator()
    date1 = datetime.date(2024, 7, 4)
    result1 = manipulator.add_30_days(date1)
    print(result1.strftime('%Y-%m-%d'))