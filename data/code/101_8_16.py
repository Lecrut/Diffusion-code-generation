import calendar

class WeekdayConverter:

    def __init__(self):
        self.weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    def get_weekday(self, year, month, day):
        weekday_num = calendar.weekday(year, month, day)
        return self.weekdays[weekday_num]
if __name__ == '__main__':
    converter = WeekdayConverter()
    print(converter.get_weekday(2023, 10, 26))
    print(converter.get_weekday(2023, 10, 27))