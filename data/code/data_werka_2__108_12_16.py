from datetime import datetime

class DayExtractor:
    def __init__(self, timestamp_str: str):
        self._dt = datetime.fromisoformat(timestamp_str)

    def get_day(self) -> int:
        return self._dt.day

    def get_month(self) -> int:
        return self._dt.month

    def get_year(self) -> int:
        return self._dt.year

if __name__ == '__main__':
    raw_ts = '2024-07-04T12:00:00'
    extractor = DayExtractor(raw_ts)
    print(extractor.get_day())
    print(extractor.get_month())
    print(extractor.get_year())