from datetime import datetime
from typing import Tuple

class DateTimeExtractor:
    DAY_PATTERN = '%Y-%m-%dT%H:%M:%S'
    SAMPLE_TIMESTAMP = '2024-07-04T12:00:00'

    @staticmethod
    def parse_to_datetime(timestamp: str) -> datetime:
        return datetime.strptime(timestamp, DateTimeExtractor.DAY_PATTERN)

    @staticmethod
    def extract_day(timestamp: str) -> int:
        dt_obj = DateTimeExtractor.parse_to_datetime(timestamp)
        return dt_obj.day

if __name__ == '__main__':
    sample_time = DateTimeExtractor.SAMPLE_TIMESTAMP
    extracted_day = DateTimeExtractor.extract_day(sample_time)
    print(extracted_day)