from dateutil import parser

class DateParser:
    def __init__(self, date_str):
        self.date_obj = parser.parse(date_str)

    def get_day_of_week(self):
        return self.date_obj.strftime('%A')

if __name__ == '__main__':
    sample_date = 'January 15, 2023'
    date_parser = DateParser(sample_date)
    day_of_week = date_parser.get_day_of_week()
    print(day_of_week)