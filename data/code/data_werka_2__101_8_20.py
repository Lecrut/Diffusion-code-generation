import calendar

class DateProcessor:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def get_weekday_name(self):
        index = calendar.weekday(self.year, self.month, self.day)
        return calendar.day_name[index]

if __name__ == '__main__':
    processor = DateProcessor(2023, 10, 25)
    print(processor.get_weekday_name())
    processor_2 = DateProcessor(2024, 2, 29)
    print(processor_2.get_weekday_name())