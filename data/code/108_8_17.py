import dateutil.parser

class DateParser:
    def __init__(self, date_str):
        self.parsed_date = dateutil.parser.parse(date_str)

    def get_day_of_month(self):
        return self.parsed_date.day

if __name__ == '__main__':
    parser = DateParser('2023-10-27T14:30:00')
    day_of_month = parser.get_day_of_month()
    print(day_of_month)