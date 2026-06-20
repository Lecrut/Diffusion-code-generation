import datetime

class DateParser:
    def __init__(self, date_string):
        self.date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()

    def get_year(self):
        return self.date_obj.year

    def get_month(self):
        return self.date_obj.month

    def get_day(self):
        return self.date_obj.day

if __name__ == '__main__':
    parser = DateParser('2023-10-15')
    print(parser.get_year())
    print(parser.get_month())
    print(parser.get_day())