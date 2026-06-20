from dateutil import parser

class DateParser:
    @staticmethod
    def get_day_of_month(date_string):
        parsed_date = parser.parse(date_string)
        return parsed_date.day

if __name__ == '__main__':
    sample_date_str = "2023-10-27T14:30:00"
    day_of_month = DateParser.get_day_of_month(sample_date_str)
    print(day_of_month)