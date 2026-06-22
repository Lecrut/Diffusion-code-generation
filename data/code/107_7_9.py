from datetime import datetime, timezone

class TimestampConverter:
    FORMAT_STRING = '%Y-%m-%dT%H:%M:%SZ'
    UTC = timezone.utc

    @staticmethod
    def to_iso_string(unix_timestamp: float) -> str:
        utc_time = datetime.fromtimestamp(unix_timestamp, tz=TimestampConverter.UTC)
        return utc_time.strftime(TimestampConverter.FORMAT_STRING)

if __name__ == '__main__':
    converter = TimestampConverter()
    samples = [1609459200, 1700000000, 0]
    for ts in samples:
        result = converter.to_iso_string(ts)
        print(result)