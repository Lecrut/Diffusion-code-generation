import datetime

class DateProcessor:
    def __init__(self, date_string):
        self.date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')

    def get_day_of_week(self):
        return self.date_obj.strftime('%A')

if __name__ == '__main__':
    processor = DateProcessor('2023-10-05')
    day_of_week = processor.get_day_of_week()
    print(day_of_week)