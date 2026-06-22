from datetime import datetime, timedelta, timezone

class TimezoneFormatter:
    def __init__(self, offset_minutes: int):
        if not isinstance(offset_minutes, int):
            raise TypeError("Offset must be an integer")
        if offset_minutes < -1440 or offset_minutes > 1440:
            raise ValueError("Offset minutes out of valid range")
        self.offset_minutes = offset_minutes

    def format(self, dt: datetime) -> str:
        if dt.tzinfo is not None:
            raise ValueError("Input datetime must be naive")
        
        total_offset = timedelta(minutes=self.offset_minutes)
        sign = '+' if self.offset_minutes >= 0 else '-'
        abs_minutes = abs(self.offset_minutes)
        
        hours = abs_minutes // 60
        minutes = abs_minutes % 60
        
        offset_part = f"{sign}{hours:02d}{minutes:02d}"
        dt_part = dt.strftime('%Y-%m-%dT%H:%M:%S')
        
        return f"{dt_part}{offset_part}"

if __name__ == '__main__':
    formatter = TimezoneFormatter(330)
    naive_dt = datetime(2023, 10, 15, 14, 30, 0)
    result = formatter.format(naive_dt)
    print(result)