from datetime import datetime, timezone

class TimestampDiffCalculator:
    def __init__(self, ts1: str, ts2: str):
        self.ts1 = ts1
        self.ts2 = ts2
        self.dt1 = self._parse(ts1)
        self.dt2 = self._parse(ts2)
        self.diff = self.dt2 - self.dt1

    def _parse(self, ts: str) -> datetime:
        if ts.endswith('Z'):
            ts = ts[:-1] + '+00:00'
        return datetime.fromisoformat(ts)

    def get_seconds(self) -> float:
        return self.diff.total_seconds()

    def get_minutes(self) -> float:
        return self.get_seconds() / 60

    def get_hours(self) -> float:
        return self.get_seconds() / 3600

if __name__ == '__main__':
    calc = TimestampDiffCalculator("2023-01-01T00:00:00Z", "2023-01-02T12:30:00Z")
    print(calc.get_seconds())
    print(calc.get_minutes())
    print(calc.get_hours())