from datetime import datetime, timedelta

class DateTimeFormatter:
    @staticmethod
    def format_datetime_with_offset(dt):
        utc_offset = dt.utcoffset()
        offset_minutes = utc_offset.total_seconds() / 60
        offset_hours = int(offset_minutes / 60)
        offset_minutes_remaining = abs(int(offset_minutes) % 60)
        offset_str = f"+{offset_hours:02d}{offset_minutes_remaining:02d}"
        return dt.strftime('%Y-%m-%d %H:%M') + offset_str

if __name__ == '__main__':
    formatter = DateTimeFormatter()
    naive_dt1 = datetime(2023, 4, 15, 12, 0)
    naive_dt2 = datetime(2023, 4, 15, 12, 0, tzinfo=timedelta(hours=2))
    print(formatter.format_datetime_with_offset(naive_dt1))
    print(formatter.format_datetime_with_offset(naive_dt2))