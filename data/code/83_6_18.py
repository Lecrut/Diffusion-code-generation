from datetime import date

class DatePairGenerator:
    def __init__(self, dates):
        self.dates = dates
        self.index = 0

    @staticmethod
    def are_dates_equal(date1, date2):
        return date1 == date2

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.dates) - 1:
            current_date = self.dates[self.index]
            next_date = self.dates[self.index + 1]
            self.index += 1
            return self.are_dates_equal(current_date, next_date)
        else:
            raise StopIteration

if __name__ == '__main__':
    dates = [date(2023, 10, 27), date(2023, 10, 27), date(2023, 11, 27)]
    generator = DatePairGenerator(dates)
    
    for result in generator:
        print(result)