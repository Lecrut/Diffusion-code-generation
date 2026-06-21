from datetime import datetime

class DateExtractor:
    def __init__(self, timestamp: str):
        self.timestamp = timestamp
        self.date_obj = datetime.fromisoformat(timestamp)

    def get_day(self) -> int:
        return self.date_obj.day

    def get_month(self) -> int:
        return self.date_obj.month

    def get_year(self) -> int:
        return self.date_obj.year

if __name__ == '__main__':
    sample_timestamp = '2024-07-04T12:00:00'
    extractor = DateExtractor(sample_timestamp)
    print(extractor.get_day())
    print(extractor.get_month())
    print(extractor.get_year())