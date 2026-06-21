from datetime import datetime, timedelta, timezone

class NaiveDatetimeFormatter:
    ZERO_OFFSET = timedelta(0)

    @staticmethod
    def _compute_offset_seconds(dt: datetime) -> int:
        if dt.tzinfo is not None:
            raise ValueError('Input datetime must be naive')
        utc_dt = dt.replace(tzinfo=timezone.utc)
        offset = utc_dt.utcoffset()
        if offset is None:
            return 0
        return int(offset.total_seconds())

    @classmethod
    def format_with_offset(cls, dt: datetime) -> str:
        total_seconds = cls._compute_offset_seconds(dt)
        sign = '-' if total_seconds < 0 else '+'
        abs_seconds = abs(total_seconds)
        hours = abs_seconds // 3600
        minutes = (abs_seconds % 3600) // 60
        return f'{sign}{hours:02d}{minutes:02d}'

if __name__ == '__main__':
    sample_naive_dt = datetime(2023, 10, 15, 14, 30, 0)
    formatter = NaiveDatetimeFormatter()
    result = formatter.format_with_offset(sample_naive_dt)
    print(result)