from datetime import datetime

class TimeDeltaAnalyzer:
    def __init__(self, format_string):
        self.format_string = format_string

    def parse(self, date_string):
        return datetime.strptime(date_string, self.format_string)

    def calculate_minutes(self, start_str, end_str):
        start_dt = self.parse(start_str)
        end_dt = self.parse(end_str)
        delta = end_dt - start_dt
        return delta.total_seconds() / 60.0

    def calculate_seconds(self, start_str, end_str):
        start_dt = self.parse(start_str)
        end_dt = self.parse(end_str)
        delta = end_dt - start_dt
        return delta.total_seconds()

if __name__ == '__main__':
    analyzer = TimeDeltaAnalyzer('%Y-%m-%d %H:%M:%S')
    t1 = '2023-01-01 10:00:00'
    t2 = '2023-01-01 12:30:00'
    print(analyzer.calculate_minutes(t1, t2))
    print(analyzer.calculate_seconds(t1, t2))