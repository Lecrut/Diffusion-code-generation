import datetime

class DateWeekday:
    def __init__(self, date_string):
        self.date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')

    def get_weekday(self):
        return self.date_obj.strftime('%A')

if __name__ == '__main__':
    date_instance = DateWeekday('2023-12-25')
    print(date_instance.get_weekday())