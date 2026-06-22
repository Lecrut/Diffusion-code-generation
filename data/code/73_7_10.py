from datetime import datetime

class DateDiffCalculator:
    def __init__(self, fmt='%Y-%m-%d %H:%M:%S'):
        self.fmt = fmt

    def _parse(self, date_str):
        return datetime.strptime(date_str, self.fmt)

    def difference_in_minutes(self, start_str, end_str):
        start_dt = self._parse(start_str)
        end_dt = self._parse(end_str)
        delta = end_dt - start_dt
        return delta.total_seconds() / 60.0

    def difference_in_seconds(self, start_str, end_str):
        start_dt = self._parse(start_str)
        end_dt = self._parse(end_str)
        delta = end_dt - start_dt
        return delta.total_seconds()

if __name__ == '__main__':
    calc = DateDiffCalculator()
    s1 = '2023-01-01 10:00:00'
    e1 = '2023-01-01 12:30:00'
    print(calc.difference_in_minutes(s1, e1))
    print(calc.difference_in_seconds(s1, e1))