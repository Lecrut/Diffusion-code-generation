import time

class DateAnalyzer:
    def __init__(self, date_string):
        self.date_string = date_string
        self.struct_time = time.strptime(date_string, "%Y-%m-%d")
        self.timestamp = time.mktime(self.struct_time)
        self.weekday_index = time.localtime(self.timestamp).tm_wday

    def get_weekday_name(self):
        names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return names[self.weekday_index]

    def get_timestamp(self):
        return self.timestamp

if __name__ == '__main__':
    analyzer = DateAnalyzer('2023-01-01')
    print(analyzer.get_weekday_name())
    print(analyzer.get_timestamp())