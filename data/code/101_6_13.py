from dateutil.parser import parse

class DateAnalyzer:
    def __init__(self, date_string: str):
        self.date_string = date_string
        self.parsed_date = parse(date_string)

    def get_day_of_week(self) -> str:
        return self.parsed_date.strftime('%A')

    def get_month_name(self) -> str:
        return self.parsed_date.strftime('%B')

if __name__ == '__main__':
    analyzer = DateAnalyzer('January 15, 2023')
    print(analyzer.get_day_of_week())
    print(analyzer.get_month_name())