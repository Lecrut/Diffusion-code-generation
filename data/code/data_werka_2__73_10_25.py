import datetime

UNIT_LABELS = {
    'days': 86400,
    'hours': 3600,
    'minutes': 60,
    'seconds': 1
}

class TimeCalculator:
    def diff(self, start_time, end_time):
        start_dt = self._normalize(start_time)
        end_dt = self._normalize(end_time)
        delta_seconds = int((end_dt - start_dt).total_seconds())
        if delta_seconds < 0:
            delta_seconds = -delta_seconds
        return self._format_delta(delta_seconds)

    def _normalize(self, value):
        if isinstance(value, datetime.datetime):
            return value
        if isinstance(value, str):
            return datetime.datetime.fromisoformat(value)
        raise ValueError("Unsupported time format")

    def _format_delta(self, total_seconds):
        parts = []
        for unit_name, unit_seconds in UNIT_LABELS.items():
            if total_seconds >= unit_seconds:
                count = total_seconds // unit_seconds
                total_seconds %= unit_seconds
                parts.append(f"{count} {unit_name}")
        if not parts:
            return "0 seconds"
        return ", ".join(parts)

if __name__ == '__main__':
    calc = TimeCalculator()
    start = datetime.datetime(2023, 1, 1, 10, 0, 0)
    end = datetime.datetime(2023, 1, 3, 12, 30, 45)
    result = calc.diff(start, end)
    print(result)
    result2 = calc.diff("2023-01-01T10:00:00", "2023-01-01T10:05:30")
    print(result2)