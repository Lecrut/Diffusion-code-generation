from datetime import datetime

class TimestampValidator:
    WEEKDAY_THRESHOLD: int = 5

    @staticmethod
    def is_weekday(timestamp_str: str) -> bool:
        parsed_datetime = datetime.fromisoformat(timestamp_str)
        day_index = parsed_datetime.weekday()
        return day_index < TimestampValidator.WEEKDAY_THRESHOLD

if __name__ == '__main__':
    sample_timestamp = '2023-10-07T12:00:00'
    is_weekday_result = TimestampValidator.is_weekday(sample_timestamp)
    print(is_weekday_result)