from datetime import datetime

class TimeSpanAnalyzer:
    def __init__(self, date_format: str = '%Y-%m-%d %H:%M:%S'):
        self.date_format = date_format

    def parse(self, date_string: str) -> datetime:
        return datetime.strptime(date_string, self.date_format)

    def get_difference_in_minutes(self, start_date: str, end_date: str) -> float:
        start_dt = self.parse(start_date)
        end_dt = self.parse(end_date)
        delta = end_dt - start_dt
        return delta.total_seconds() / 60

    def get_difference_in_seconds(self, start_date: str, end_date: str) -> float:
        start_dt = self.parse(start_date)
        end_dt = self.parse(end_date)
        delta = end_dt - start_dt
        return delta.total_seconds()

if __name__ == '__main__':
    analyzer = TimeSpanAnalyzer()
    start = '2024-05-10 08:00:00'
    end = '2024-05-10 14:45:00'
    minutes = analyzer.get_difference_in_minutes(start, end)
    seconds = analyzer.get_difference_in_seconds(start, end)
    print(minutes)
    print(seconds)