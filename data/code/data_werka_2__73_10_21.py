import datetime
import calendar

class TimeCalculator:
    DAYS_IN_WEEK = 7
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60
    SECONDS_IN_MINUTE = 60
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_DAY = 86400

    def _parse_timestamp(self, timestamp):
        if isinstance(timestamp, datetime.datetime):
            return timestamp
        if isinstance(timestamp, str):
            return datetime.datetime.fromisoformat(timestamp)
        raise ValueError("Unsupported timestamp type")

    def diff(self, start_time, end_time):
        start_dt = self._parse_timestamp(start_time)
        end_dt = self._parse_timestamp(end_time)
        delta = end_dt - start_dt
        total_seconds = int(delta.total_seconds())
        absolute_seconds = abs(total_seconds)
        sign = '-' if total_seconds < 0 else ''
        days = absolute_seconds // self.SECONDS_IN_DAY
        remaining_seconds = absolute_seconds % self.SECONDS_IN_DAY
        hours = remaining_seconds // self.SECONDS_IN_HOUR
        remaining_seconds = remaining_seconds % self.SECONDS_IN_HOUR
        minutes = remaining_seconds // self.MINUTES_IN_HOUR
        seconds = remaining_seconds % self.MINUTES_IN_HOUR
        parts = []
        if days > 0:
            days_label = 'day' if days == 1 else 'days'
            parts.append(f'{days} {days_label}')
        if hours > 0:
            hours_label = 'hour' if hours == 1 else 'hours'
            parts.append(f'{hours} {hours_label}')
        if minutes > 0:
            minutes_label = 'minute' if minutes == 1 else 'minutes'
            parts.append(f'{minutes} {minutes_label}')
        if seconds > 0:
            seconds_label = 'second' if seconds == 1 else 'seconds'
            parts.append(f'{seconds} {seconds_label}')
        if not parts:
            return f'{sign}0 seconds'
        return f'{sign}{", ".join(parts)}'

if __name__ == '__main__':
    calculator = TimeCalculator()
    start = datetime.datetime(2023, 1, 1, 10, 0, 0)
    end = datetime.datetime(2023, 1, 5, 14, 30, 45)
    result = calculator.diff(start, end)
    print(result)