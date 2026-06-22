from datetime import datetime

class TimestampParser:
    def __init__(self, raw: str):
        self.raw = raw
        self.parsed = datetime.fromisoformat(raw)

    def get_day(self) -> int:
        return self.parsed.day

    def get_month(self) -> int:
        return self.parsed.month

    def get_year(self) -> int:
        return self.parsed.year

if __name__ == '__main__':
    ts_str = '2024-07-04T12:00:00'
    parser = TimestampParser(ts_str)
    print(parser.get_day())
    print(parser.get_month())
    print(parser.get_year())