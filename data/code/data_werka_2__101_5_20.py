import time

class DateAnalyzer:
    def __init__(self, target_date):
        self.target_date = target_date
        self.struct_time = time.strptime(target_date, "%Y-%m-%d")
        self.timestamp = time.mktime(self.struct_time)

    def get_weekday_name(self):
        local_time = time.localtime(self.timestamp)
        weekday_map = [
            "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"
        ]
        return weekday_map[local_time.tm_wday]

    def get_timestamp(self):
        return self.timestamp

    def format_local(self):
        return time.strftime("%A, %B %d, %Y", time.localtime(self.timestamp))

if __name__ == '__main__':
    analyzer = DateAnalyzer('2023-01-01')
    print(analyzer.get_weekday_name())
    print(analyzer.get_timestamp())
    print(analyzer.format_local())