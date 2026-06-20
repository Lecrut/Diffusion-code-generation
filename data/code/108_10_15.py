import datetime

class DateAnalyzer:
    def __init__(self, date_string):
        self.date_string = date_string
        self.formats = [
            "%Y-%m-%d",
            "%m/%d/%Y",
            "%d-%m-%Y",
            "%Y/%m/%d",
            "%m-%d-%Y"
        ]
    
    def parse_date(self):
        for fmt in self.formats:
            try:
                date_obj = datetime.datetime.strptime(self.date_string, fmt)
                return date_obj
            except ValueError:
                continue
        raise ValueError(f"Could not parse date string: {self.date_string}")
    
    def get_day_of_week(self):
        date_obj = self.parse_date()
        return date_obj.strftime("%A")

if __name__ == '__main__':
    analyzer = DateAnalyzer("2024-01-01")
    print(analyzer.get_day_of_week())